print("dafsef")
import  numpy as np
import  pandas as pd
import  xgboost as xgb
from  pandas import  DataFrame,Series
data = DataFrame(np.arange(16).reshape(4,4),index=list('abcd'),columns=list('wxyz'))
print(data)
git add Test.py
git commit -f "py"
git remote add origin git@github.com:renxb/dome.git
git remote add origin git@github.com:xxse/xx.git
git remote -v
git remote rm origin
git pull --rebase origin master