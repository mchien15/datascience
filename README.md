# Find similar players using Cosine similarity

## To run on Streamlit server
Click this [link](https://datascience-cvxlqzzers7ydppnahpgbf.streamlit.app/)

## To run locally

### Clone the repo
```
git clone https://github.com/mchien15/datascience.git
```

### Install required packages
```
pip install -r requirements.txt
```

### Data pre-processing
Run this line to clean and process all csv files from `/data` folder and merge them into `all_processed.csv`

```
python preprocess_data.py --path data/ --output all_processed.csv 
```

### Run the Streamlit app

```
streamlit run app.py
```

Visit the URL displayed in the terminal (usually http://localhost:8501) to interact with the app