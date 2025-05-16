import argparse
import sys

sys.path.append('./options')
from trainer import Trainer
from Conv_TasNet import ConvTasNet
from DataLoaders import make_dataloader
from option import parse
from utils import get_logger

def main():
    # Reading option
    parser = argparse.ArgumentParser()

    parser.add_argument('--opt', type=str, help='Path to option YAML file.', default="./train.yml")
    args = parser.parse_args()

    print(1)

    opt = parse(args.opt, is_tain=True)
    logger = get_logger(__name__)

    logger.info('Building the model of Conv-TasNet')
    net = ConvTasNet(**opt['net_conf'])

    print(2)

    logger.info('Building the trainer of Conv-TasNet')
    gpuid = tuple(opt['gpu_ids'])
    trainer = Trainer(net, **opt['train'], resume=opt['resume'],
                      gpuid=gpuid, optimizer_kwargs=opt['optimizer_kwargs'])

    print(3)

    logger.info('Making the train and test data loader')
    train_loader = make_dataloader(is_train=True, data_kwargs=opt['datasets']['train'], num_workers=opt['datasets']
    ['num_workers'], chunk_size=opt['datasets']['chunk_size'], batch_size=opt['datasets']['batch_size'])
    val_loader = make_dataloader(is_train=False, data_kwargs=opt['datasets']['val'], num_workers=opt['datasets']
    ['num_workers'], chunk_size=opt['datasets']['chunk_size'], batch_size=opt['datasets']['batch_size'])

    train_len = sum(1 for _ in train_loader)
    val_len = sum(1 for _ in val_loader)
    logger.info('Train data loader: {}, Test data loader: {}'.format(train_len, val_len))

    print(4)

    trainer.run(train_loader, val_loader)

    print(5)


if __name__ == "__main__":
    main()
