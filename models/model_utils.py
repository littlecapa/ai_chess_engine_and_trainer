import torch
import os
import logging
import shutil

#
# Adapted from https://github.com/cs230-stanford/cs230-code-examples/blob/master/pytorch/nlp/utils.py
#

def get_file_name(model):
    return "chkp_" + model.get_name() + ".h5"

def save_checkpoint(epoch, model, optimizer, checkpoint_dir):
    """Saves model and training parameters at checkpoint + 'last.pth.tar'. If is_best==True, also saves
    checkpoint + 'best.pth.tar'

    Args:
        state: (dict) contains model's state_dict, may contain other keys such as epoch, optimizer state_dict
        is_best: (bool) True if it is the best model seen till now
        checkpoint: (string) folder where parameters are to be saved
    """
    state = {'epoch': epoch + 1,
            'hash': model.get_hash(), 
            'state_dict': model.state_dict(),
            'optim_dict' : optimizer.state_dict()}
    filename = get_file_name(model)
    filepath = os.path.join(checkpoint_dir, filename)
    if not os.path.exists(checkpoint_dir):
        logging.debug("Checkpoint Directory does not exist! Making directory {}".format(checkpoint_dir))
        os.mkdir(checkpoint_dir)
    else:
        logging.debug("Checkpoint Directory exists! ")
    torch.save(state, filepath)


def load_checkpoint(checkpoint_dir, model, optimizer=None):
    """Loads model parameters (state_dict) from file_path. If optimizer is provided, loads state_dict of
    optimizer assuming it is present in checkpoint.

    Args:
        checkpoint: (string) filename which needs to be loaded
        model: (torch.nn.Module) model for which the parameters are loaded
        optimizer: (torch.optim) optional: resume optimizer from checkpoint
    """
    if not os.path.exists(checkpoint):
        raise ("File doesn't exist {}".format(checkpoint))
    checkpoint = torch.load(checkpoint)
    model.load_state_dict(checkpoint['state_dict'])

    if optimizer:
        optimizer.load_state_dict(checkpoint['optim_dict'])

    return checkpoint