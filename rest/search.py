import openai
from openai.embeddings_utils import get_embedding, cosine_similarity

# https://github.com/openai/openai-cookbook/blob/main/examples/Obtain_dataset.ipynb
# https://github.com/openai/openai-cookbook/blob/main/examples/data/fine_food_reviews_1k.csv

import pandas as pd
import numpy as np

openai.api_key = "{key}"


# search through the reviews for a specific product
def search_reviews(df, product_description, n=3, pprint=True):
    product_embedding = get_embedding(
        product_description,
        engine="text-embedding-ada-002"
    )
    df["similarity"] = df.embedding.apply(lambda x: cosine_similarity(x, product_embedding))

    results = (
        df.sort_values("similarity", ascending=False)
        .head(n)
        .combined.str.replace("Title: ", "")
        .str.replace("; Content:", ": ")
    )
    if pprint:
        for r in results:
            print(r[:200])
            print()
    return results


input_datapath = "data/fine_food_reviews_with_embeddings_1k.csv"  # to save space, we provide a pre-filtered dataset
mydf = pd.read_csv(input_datapath, index_col=0)
mydf["embedding"] = mydf.embedding.apply(eval).apply(np.array)
print(mydf.embedding)

results = search_reviews(mydf, "delicious beans", n=3)
print(results)