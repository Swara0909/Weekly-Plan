import pandas as pd
data=pd.DataFrame({
    "spam":[1,1,0,1,0],
    "link":[0,0,1,1,1]
})

spam=data[data["spam"]==1]
prob_link_given_spam=(spam["link"]==1).mean()
print(prob_link_given_spam)