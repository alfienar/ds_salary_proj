import glassdoor_scraping as gs
import pandas as pd

path = "C:/Users/USER/Desktop/Project/data-science/ds_salary_proj/chromedriver"

df = gs.get_jobs('data scientist', 15, False, path, 15)