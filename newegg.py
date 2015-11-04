import urllib2
import re
import HTMLParser
import os
import sys

# Get item
def getItem(contents, attribute):
	searchString = "%s:(.*?)," % attribute
	search = re.compile(searchString)
	item = search.search(contents)
	item = item.group(1)
	item = item[2:-2]
	item = HTMLParser.HTMLParser().unescape(item)
	return item

# Clear the screen
os.system('clear') # Linux / OS X
	
# Set links for stores
neweggURL = 'http://www.newegg.com/Product/Product.aspx?Item='

# Get SKU from arguments or user prompt
if len(sys.argv) > 1:
	SKU = sys.argv[1]
else:
	SKU = raw_input('Enter SKU: ')

# Generate URL
url = neweggURL + SKU

# Get page
aResp = urllib2.urlopen(url);
contents = aResp.read();

# Find specific attributes
price = getItem(contents, 'product_sale_price')
mainCategory = getItem(contents, 'product_category_name')
subCategory = getItem(contents, 'product_subcategory_name')
product = getItem(contents, 'product_title')

print ""
print "Newegg"
print "======"
print mainCategory
print subCategory
print "======"
print product
print "======"
print "$%s" % price
print ""