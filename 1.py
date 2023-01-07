import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df = pd.Series([0.25,0.5,0.6,0.9])
df.plot()
plt.show()
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

fig,axes = plt.subplots(2,1)
data = pd.Series([0.5,4,2,5,0.8], index=list('abcde'))
data.plot.bar(ax=axes[0], color= 'k', alpha =0.8)
data.plot.barh(ax=axes[1], color= 'k', alpha =0.8)
plt.show()
