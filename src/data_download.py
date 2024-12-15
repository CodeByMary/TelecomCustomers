import os
import subprocess
import zipfile
import logging
import shutil

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def download_and_extract_kaggle_dataset(dataset: str, folder_name: str, force_redownload=False):
    """
    Downloads a Kaggle dataset as a zip file into the specified folder and extracts it.
    Optionally, force re-download of the dataset.

    Parameters:
    dataset (str): The dataset identifier from Kaggle (e.g., 'tarekmuhammed/telecom-customers').
    folder_name (str): The folder where the dataset will be downloaded and extracted.
    force_redownload (bool): Whether to force the re-download of the dataset (default is False).
    """
    try:
        # Check if dataset already exists
        zip_file_name = dataset.split('/')[-1] + '.zip'
        zip_file_path = os.path.join(folder_name, zip_file_name)
        extracted_folder_path = os.path.join(folder_name, dataset.split('/')[-1])

        if not force_redownload and os.path.exists(extracted_folder_path):
            logging.info(f"Dataset already exists in '{folder_name}', skipping download.")
            return  # Skip download and extraction

        # Remove the existing folder and zip file if they exist (if force_redownload is True)
        if os.path.exists(folder_name):
            logging.info(f"Removing existing folder '{folder_name}' and its contents.")
            shutil.rmtree(folder_name)

        # Create the folder if it doesn't exist
        os.makedirs(folder_name)
        logging.info(f"Folder '{folder_name}' created successfully.")

        # Download the dataset
        logging.info(f"Starting dataset download: {dataset}")
        download_cmd = f'kaggle datasets download -d {dataset} -p {folder_name}'
        subprocess.run(download_cmd, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        logging.info(f"Dataset '{dataset}' downloaded successfully into '{folder_name}'.")

        # Extract the zip file
        if os.path.exists(zip_file_path):
            logging.info(f"Extracting '{zip_file_path}' into '{folder_name}'.")
            with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
                zip_ref.extractall(folder_name)
            logging.info(f"Extraction of '{zip_file_path}' completed successfully.")
        else:
            raise FileNotFoundError(f"Zip file '{zip_file_path}' not found.")
    
    except subprocess.CalledProcessError as e:
        logging.error(f"Error downloading dataset: {e.stderr.decode('utf-8')}")
        raise
    except FileNotFoundError as fnf_error:
        logging.error(f"File error: {fnf_error}")
        raise
    except zipfile.BadZipFile as bz_error:
        logging.error(f"Bad zip file error: {bz_error}")
        raise
    except OSError as e:
        logging.error(f"Error creating folder '{folder_name}': {e}")
        raise

