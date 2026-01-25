
from databricks.sdk.runtime import *

def read_csv_by_me(url):
    return (spark.read
                .format('csv')
                .options(inferSchema= True,
                        header = True,
                        sep = '|')
                .load(url))