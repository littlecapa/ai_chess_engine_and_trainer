import logging
import torch

def verify_tensor(int_tensor, size):
    # Check if the input tensor has the correct shape (size)
    if int_tensor.shape != torch.Size([size]):
        logging.error(f"Int Tensor Shape: {int_tensor.shape}")
        logging.error(f"Int Tensor Value: {int_tensor}")
        logging.error(f"Int Tensor Type: {int_tensor.dtype}")
        raise ValueError("Input tensor must have torch.Size([13])")

def convert_int64_to_bool(int64_tensor):
    verify_tensor(int64_tensor, 13)
    # Create a boolean tensor with size (13x64)
    boolean_tensor = (int64_tensor.unsqueeze(1) & (1 << torch.arange(64).to(int64_tensor.device))) > 0
    # Reshape the boolean tensor to size (832)
    boolean_tensor = boolean_tensor.view(-1)
    return boolean_tensor

def convert_int64_to_int32(int64_tensor):
    verify_tensor(int64_tensor, 13)
    # Convert the int64 tensor to a list of int64 values
    int64_values = int64_tensor.squeeze().tolist()

    # Initialize an empty list to store the int32 values
    int32_values = []

    # Convert each int64 value to two int32 values
    for int64_value in int64_values:
        # Convert the int64 value to 8 bytes (64 bits)
        bytes_64 = int64_value.to_bytes(8, byteorder='big', signed=True)
        # Convert the 4-byte chunks to int32 values
        int32_value_1 = int.from_bytes(bytes_64[:4], byteorder='big', signed=True)
        int32_value_2 = int.from_bytes(bytes_64[4:], byteorder='big', signed=True)

        # Append the int32 values to the list
        int32_values.append(int32_value_1)
        int32_values.append(int32_value_2)

    # Convert the list of int32 values to a 26x1 int32 tensor
    int32_tensor = torch.tensor(int32_values, dtype=torch.int32)
    #.unsqueeze(1)
    logging.debug(f"Int32 Tensor Shape: {int32_tensor.shape}")
    logging.debug(f"Int32 Tensor Value: {int32_tensor}")
    logging.debug(f"Int64 Tensor Value: {int64_tensor}")

    return int32_tensor

def convert_int32_to_int64(int32_tensor):
    verify_tensor(int32_tensor, 26)
    int32_values = int32_tensor.squeeze().tolist()
    int64_values = []

    for i in range(0, len(int32_values), 2):
        int32_value_1 = int32_values[i]
        int32_value_2 = int32_values[i + 1]
        
        bytes_64 = bytearray()
        bytes_64.extend(int32_value_1.to_bytes(4, byteorder='big', signed=True))
        bytes_64.extend(int32_value_2.to_bytes(4, byteorder='big', signed=True))
        
        int64_value = int.from_bytes(bytes_64, byteorder='big', signed=True)
        int64_values.append(int64_value)

    int64_tensor = torch.tensor(int64_values, dtype=torch.int64)
    #.unsqueeze(1)
    logging.debug(f"Int64 Tensor Shape: {int64_tensor.shape}")
    logging.debug(f"Int64 Tensor Value: {int64_tensor}")
    logging.debug(f"Int32 Tensor Value: {int32_tensor}")

    return int64_tensor
