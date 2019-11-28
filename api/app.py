from eve import Eve
import sys

app = Eve()
print(sys.path)
app.run(debug=True)

