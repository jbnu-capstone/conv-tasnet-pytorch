import os
import torch
import sys
sys.path.append('./options')
from AudioReader import AudioReader, write_wav
import argparse
from Conv_TasNet import ConvTasNet
from utils import get_logger
from option import parse
import tqdm


class Separation():
    def __init__(self, mix_path, yaml_path, model, gpuid):
        super(Separation, self).__init__()
        self.mix = AudioReader(mix_path, sample_rate=16000)
        opt = parse(yaml_path, is_tain=False)
        net = ConvTasNet(**opt['net_conf'])
        dicts = torch.load(model, map_location='cpu')
        net.load_state_dict(dicts["model_state_dict"])
        self.logger = get_logger(__name__)
        self.logger.info('Load checkpoint from {}, epoch {: d}'.format(model, dicts["epoch"]))
        self.net=net.cuda()
        self.device=torch.device('cuda:{}'.format(
            gpuid[0]) if len(gpuid) > 0 else 'cpu')
        self.gpuid=tuple(gpuid)

    def inference(self, file_path):
        with torch.no_grad():
            for key, egs in tqdm.tqdm(self.mix):
                #self.logger.info("Compute on utterance {}...".format(key))
                egs=egs.to(self.device)
                norm = torch.norm(egs,float('inf'))
                if len(self.gpuid) != 0:
                    ests=self.net(egs)
                    spks=[torch.squeeze(s.detach().cpu()) for s in ests]
                else:
                    ests=self.net(egs)
                    spks=[torch.squeeze(s.detach()) for s in ests]
                index=0
                for s in spks:
                    s = s[:egs.shape[0]]
                    #norm
                    s = s*norm/torch.max(torch.abs(s))
                    index += 1
                    os.makedirs(file_path+'/spk'+str(index), exist_ok=True)
                    filename=file_path+'/spk'+str(index)+'/'+key
                    write_wav(filename, s, 8000)
            self.logger.info("Compute over {:d} utterances".format(len(self.mix)))


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument(
        '-mix_scp', type=str, default='./dataset/create_scp/tt_mix.scp', help='Path to mix scp file.')
    parser.add_argument(
        '-yaml', type=str, default='./train.yml', help='Path to yaml file.')
    parser.add_argument(
        '-model', type=str, default='./best.pt', help="Path to model file.")
    parser.add_argument(
        '-gpuid', type=str, default='0', help='Enter GPU id number')
    parser.add_argument(
        '-save_path', type=str, default='./non-pit-2', help='save result path')
    args=parser.parse_args()
    gpuid=[int(i) for i in args.gpuid.split(',')]
    separation=Separation(args.mix_scp, args.yaml, args.model, gpuid)
    separation.inference(args.save_path)


if __name__ == "__main__":
    main()