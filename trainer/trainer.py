import logging
import torch
from trainer.eval_net_KRk import Eval_Net_KRk
from trainer.trainer_data_loader import Trainer_Data_Set
from math import sqrt

class Chess_Trainer():

  INIT_HASH = 0

  def __init__(self, train_data_file, first_training = False, filename = "chess.h5", learning_rate = 1e-2):
    self.train_dataset = Trainer_Data_Set(train_data_file)
    #self.test_data_loader = torch.utils.data.DataLoader(self.train_dataset, batch_size=1, shuffle=False)
    self.filename = filename
    self.learning_rate = learning_rate
    self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    self.init_components()
    self.hash = self.INIT_HASH
    if not first_training:
      self.resume(eval = False)

  def init_components(self):
    self.machine = Eval_Net_KRk()
    self.machine.to(self.device)
    self.optimizer = torch.optim.Adam(self.machine.parameters(), self.learning_rate, weight_decay=1e-5)
    self.criterion = torch.nn.MSELoss(reduction='mean')
    torch.backends.cudnn.enabled = True

  def rest(self):
    torch.save(self.machine.state_dict(), self.filename)
    self.hash = self.machine.get_hash_value()
    print(f"Resting Hash: {self.hash}")
    self.machine.eval()
    self.do_baseline_testing()
    self.machine = None

  def resume(self, eval = True):
    self.init_components()
    self.machine.load_state_dict(torch.load(self.filename))
    new_hash = self.machine.get_hash_value()
    print(f"Resuming Hash: {new_hash}")
    if self.hash != self.INIT_HASH:
        if self.hash != self.hash:
            logging.error(f"Old hash: {self.hash}, New Hash: {new_hash}")
    self.hash = new_hash
    if eval:
        self.machine.eval()
    else:
        self.machine.train()
  
  def run_machine(self, loader, training = False):
    if training:
      self.machine.train()
    else:
       self.machine.eval()
    running_loss = 0.0
    index = 0
    for x, y, _ in loader:
      index += 1
      x = x.to(self.device).float()
      y = y.to(self.device).float()
      outputs = self.machine(x)
      loss = self.criterion(outputs, y)
      if training:
        loss.backward()
        self.optimizer.step()
        self.optimizer.zero_grad()
      running_loss += loss.item()
    return running_loss        

  def do_training(self, batch_size = 1, train_size = 0.95, num_epochs = 10, shuffle = False):

    train_size = int(train_size * len(self.train_dataset))
    val_size = len(self.train_dataset) - train_size        
    train_dataset, val_dataset = torch.utils.data.random_split(self.train_dataset, [train_size, val_size])
    train_loader = torch.utils.data.DataLoader(train_dataset, batch_size=batch_size, shuffle=shuffle)
    val_loader = torch.utils.data.DataLoader(val_dataset, batch_size=batch_size, shuffle=shuffle)
    sum_loss = 0
    for epoch in range(num_epochs):
        running_loss = self.run_machine(train_loader, training = True)
        sum_loss += running_loss
        logging.info(f'Training Results! Epoch:{epoch}, Running Loss:{int(running_loss)}, Items: {int((len(train_dataset)))}, Avg: {round(running_loss/(len(train_dataset)),2)} {round(sqrt(running_loss/(len(train_dataset))),2)}')
        self.do_validation(val_loader)
    self.rest()

  def do_validation(self, val_loader):
    with torch.no_grad():
      running_loss = self.run_machine(val_loader, training = False)
    logging.info(f'Validation Results! Running Loss:{running_loss}, Items: {len(val_loader)}, Avg: {running_loss/len(val_loader)}')
