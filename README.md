# Find similar players using Cosine and KNN

## To run locally

### Required packages
Run this line to install the required packages

```
pip install -r requirement.txt
```

### Data processing
Run this line to clean and process all csv files from `/data` folder and merge them into `all_processed.csv`

```
python preprocess_data.py --path data/ --output all_processed.csv 
```

### Run the Streamlit app using the command

```
streamlit run app.py
```

Visit the URL displayed in the terminal (usually http://localhost:8501) to interact with the app