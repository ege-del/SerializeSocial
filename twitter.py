from lxml import html
import sys
import requests
import json

#error [1] data held in ram(javascript) no dom access

bio_name = "/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/div/div/div[2]/div[1]/div/div[1]/div/div"
bio_id = "/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/div/div/div[2]/div[1]/div/div[2]/div/div/div/span"
bio_desc = "/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/div/div/div[3]/div/div"
bio_work = "/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/div/div/div[4]/div/span[1]/span/span"
bio_join_date = "/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/div/div/div[4]/div/span[3]/span"
bio_location = "/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/div/div/div[4]/div/span[2]/span/span"
bio_link = "/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/div/div/div[4]/div/a/span"
bio_following_count = "/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/div/div/div[5]/div[1]/a/span[1]/span"
bio_follower_count = "/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/div/div/div[5]/div[2]/a/span[1]/span"


tweet_dom_array = "//article[@data-testid='tweet']"

tweet_link = "./div/div/div/div[2]/div[2]/div[1]/div/div/div[1]/div/div/div[2]/div/div[3]/a"
tweet_link_2 = "/html/head/link[22]"


user_id = "./div/div/div/div[2]/div[2]/div[1]/div/div/div[1]/div/div/div[2]/div/div[1]/a/div/span"
has_checkmark = "./div/div/div/div[2]/div[2]/div[1]/div/div/div[1]/div/div/div[1]/div/a/div/div[2]/svg"
user_name = "./div/div/div/div[2]/div[2]/div[1]/div/div/div[1]/div/div/div[1]/div/a/div/div[1]/span/span"
date = "./div/div/div/div[2]/div[2]/div[1]/div/div/div[1]/div/div/div[2]/div/div[3]/a/time"
date_2 = "./div/div/div/div[3]/div[5]/div/div[1]/div/a[1]/time"
tweet_text = "./div/div/div/div[2]/div[2]/div[2]/div[1]/div"
tweet_text_2 = "./div/div/div/div[3]/div[2]/div/div"
tweet_text_3 = "./div/div/div/div[2]/div[2]/div[2]/div[2]/div"
#tweets with image use this hierarchy
reply_count = "./div/div/div/div[2]/div[2]/div[2]/div[3]/div/div[1]/div/div/div[2]/span/span/span"
reply_count_2 = "./div/div/div/div[2]/div[2]/div[2]/div[2]/div/div[1]/div/div/div[2]/span/span/span"

retweet_count = "./div/div/div/div[3]/div[6]/div/div[1]/div/a/div/span/span/span"
retweet_count_2 = "./div/div/div/div[2]/div[2]/div[2]/div[3]/div/div[2]/div/div/div[2]/span/span/span"

quote_count = "./div/div/div/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div/div[2]/span/span/span"
quote_count_2 = "./div/div/div/div[3]/div[6]/div/div[2]/div/a/div/span/span/span"


#tweets with image use this hierarchy
like_count = "./div/div/div/div[2]/div[2]/div[2]/div[3]/div/div[3]/div/div/div[2]/span/span/span"
like_count_2 = "./div/div/div/div[2]/div[2]/div[2]/div[2]/div/div[3]/div/div/div[2]/span/span/span"
like_count_3 = "./div/div/div/div[3]/div[6]/div/div[3]/div/a/div/span/span/span"

is_retweet = "./div/div/div/div[1]/div/div/div/div/div[2]/div/div/div/a"
is_promoted_tweet = "./div/div/div/div[2]/div[2]/div[2]/div[4]/div/div/span"
is_qoute_tweet = "./div/div/div/div[2]/div[2]/div[2]/div[2]/div/div[1]/span"
is_main_tweet_check = "/html/head/title"

#not tested
replying_to_banner = "./div/div/div/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[2]/div[1]"
replying_to_banner_2 = "./div/div/div/div[2]/div[2]/div[2]/div[1]"

video_blob = "./div/div/div/div[2]/div[2]/div[2]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[2]/div/div[1]/div/video"
video_blob_2 = "./div/div/div/div[3]/div[3]/div/div/div/div/div/div/div/div[2]/div/div/div/div[2]/div/div[1]/div/video"
image_links = "./div/div/div/div[3]/div[3]//img"
#"./div/div/div/div[2]/div[2]/div[2]/div[2]/div//img"

featured_link = "./div/div/div/div[2]/div[2]/div[2]/div[2]/div/div[1]/a"


quote_tweet_id = "./div/div/div/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[1]/div/div/div/div/div/div[2]/div[1]/div/div/div/span"
quote_tweet_name = "./div/div/div/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[1]/div/div/div/div/div/div[1]/div/div/div[2]/span/span"
quote_tweet_text = "./div/div/div/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[2]/div[2]"
quote_tweet_video_blob = "./div/div/div/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[3]/div/div/div/div/div/div[2]/div/div/div/div[2]/div/div[1]/div/video"

quote_tweet_checkmark = "./div/div/div/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[1]/div/div/div/div/div/div[1]/div/div/div[3]/svg"
quote_tweet_date = "./div/div/div/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[1]/div/div/div/div/div/div[2]/div[2]/div[2]/div/time"
quote_tweet_link = "./div/div/div/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[3]/div/div/div/div[2]/div/div[2]/div/a"
quote_tweet_image_links = "./div/div/div/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[3]/div"


def text_content_macro(root_element,xpaths):
	for xpath in xpaths:
		if len(root_element.xpath(xpath)) > 0:
			return root_element.xpath(xpath)[0].text_content()
	return "error"

def attribute_check_macro(root_element,xpaths,attribute_name,attribute_value):
	for xpath in xpaths:
		if len(root_element.xpath(xpath)) > 0:
			if attribute_name in root_element.xpath(xpath)[0].attrib and root_element.xpath(xpath)[0].attrib[attribute_name] == attribute_value:
				return root_element.xpath(xpath)[0]
	return "error"

def iterate_tweets(tweets_dom):
	tweets = {'tweets':[]}
	for tweet in tweets_dom:
		result = serializeTweet(tweet)
		if result:
			tweets["tweets"].append(result)

	return tweets

def serializeNumber(nt):
	if "K" in nt:
		if "K" in nt.split(".")[1]:
			return int(nt.split(".")[0] + nt.split(".")[1].replace("K","") + "00")
		else:
			return int(nt.replace("K","000"))
	else:
		return int(nt.replace(".","").replace(",",""))

def serializeBio(page_element):
	bio = {}
	bio["name"] = page_element.xpath(bio_name)[0].text_content()
	bio["id"] = page_element.xpath(bio_id)[0].text_content()
	bio["work"] = page_element.xpath(bio_work)[0].text_content()
	bio["join_date"] = page_element.xpath(bio_join_date)[0].text_content().replace("Joined ","")
	bio["location"] = page_element.xpath(bio_location)[0].text_content()
	bio["link"] = page_element.xpath(bio_link)[0].text_content()

	bio["following_count"] = serializeNumber(page_element.xpath(bio_following_count)[0].text_content())
	bio["follower_count"] = serializeNumber(page_element.xpath(bio_follower_count)[0].text_content())

	return bio

def serializeTweet(h_element):
	tweet = {}

	tweet["user_id"] = h_element.xpath(user_id)[0].text_content().replace("@","")
	tweet["has_checkmark"] =  len(h_element.xpath(has_checkmark)) > 0
	tweet["user_name"] = h_element.xpath(user_name)[0].text_content()


	if len(h_element.xpath(tweet_link)) == 0:
		if len(h_element.xpath(is_main_tweet_check)) > 0 and tweet["user_name"] in  h_element.xpath(is_main_tweet_check)[0].text_content():
			if h_element.xpath(tweet_link_2)[0].attrib["data-rh"] == "true":
				tweet["tweet_link"] = h_element.xpath(tweet_link_2)[0].attrib["href"]
			else:
				tweet["tweet_link"] = "error [-1]"	
		else:
			tweet["tweet_link"] = "error [2]"
	else:
		tweet["tweet_link"] = h_element.xpath(tweet_link)[0].attrib['href']


	if len(h_element.xpath(date)) > 0:
		tweet["date"] =  h_element.xpath(date)[0].attrib['datetime']
	elif len(h_element.xpath(date_2)) > 0:
		tweet["date"] =  h_element.xpath(date_2)[0].attrib['datetime']
	else:
		tweet["date"] = "error"

	found_element = attribute_check_macro(h_element,[tweet_text,tweet_text_2,tweet_text_3],"data-testid","tweetText")
	if found_element != "error":
		buf_str = ""
		for i in found_element:
			print(i)
			z = i
			if z.tag == "span" or z.tag == "div" or z.tag == "a":
				print(z.tag)
				print(z.text_content())
				buf_str += z.text_content()
			if z.tag == "img":
				buf_str += z.attrib['alt']
		tweet["text"] = buf_str

	res = text_content_macro(h_element,[reply_count,reply_count_2])
	if res != "error":
		tweet["reply_count"] = serializeNumber(res)
	else:
		tweet["reply_count"] = -1

	res = text_content_macro(h_element,[retweet_count,retweet_count_2])
	if res != "error":
		tweet["retweet_count"] = serializeNumber(res)
	else:
		tweet["retweet_count"] = -1

	res = text_content_macro(h_element,[quote_count,quote_count_2])
	if res != "error":
		tweet["quote_count"] = serializeNumber(res)
	else:
		tweet["quote_count"] = -1


	res = text_content_macro(h_element,[like_count,like_count_2,like_count_3])
	if res != "error":
		tweet["like_count"] = serializeNumber(res)
	else:
		tweet["like_count"] = -1
	

	tweet["is_retweet"] = len(h_element.xpath(is_retweet)) > 0 and "Retweeted" in h_element.xpath(is_retweet)[0].text_content()
	tweet["is_quote_tweet"] = len(h_element.xpath(is_qoute_tweet)) > 0 and h_element.xpath(is_qoute_tweet)[0].text_content() == "Quote Tweet"
	tweet["is_promoted_tweet"] = len(h_element.xpath(is_promoted_tweet)) > 0 and h_element.xpath(is_promoted_tweet)[0].text_content() == "Promoted"

	tweet["has_video"] = len(h_element.xpath(video_blob)) > 0 or len(h_element.xpath(video_blob_2)) > 0
	

	tweet["has_featured_link"] = len(h_element.xpath(featured_link)) > 0
	
	if tweet["has_featured_link"]:
		tweet["featured_link"] = h_element.xpath(featured_link)[0].attrib["href"]
	
	tweet["has_images"] = len(h_element.xpath(image_links)) > 0

	if tweet["has_images"]:
		tweet["images"] = []
		for i in h_element.xpath(image_links):
			try:
				tweet["images"].append(i.attrib['src'])
			except:
				tweet["images"] +="error"
	
	reply_info = attribute_check_macro(h_element,[replying_to_banner,replying_to_banner_2],"id","id__tlb76xjzb3j")
	
	if reply_info != "error":
		reply_info = reply_info.text_content()
		if len(reply_info.split("@")) > 2:
			tweet["thread_owner"] = reply_info.split("@")[2].split(" ")[0]
			tweet["replying_to"] = reply_info.split("@")[1].split(" ")[0]
		else:
			tweet["replying_to"] = reply_info.split("@")[1].split(" ")[0]


	if tweet["is_quote_tweet"]:
		tweet["quote_tweet"] = {}

		tweet["quote_tweet"]["has_video"] = len(h_element.xpath(quote_tweet_video_blob)) > 0

		if len(h_element.xpath(quote_tweet_link)) > 0:
			tweet["quote_tweet"]["tweet_link"] = h_element.xpath(quote_tweet_link)[0].text_content()
		else:
			tweet["quote_tweet"]["tweet_link"] = "error [1]"

		tweet["quote_tweet"]["user_id"] =  h_element.xpath(quote_tweet_id)[0].text_content()
		tweet["quote_tweet"]["has_checkmark"] = len(h_element.xpath(quote_tweet_checkmark)) > 0
		tweet["quote_tweet"]["user_name"] =  h_element.xpath(quote_tweet_name)[0].text_content()
		tweet["quote_tweet"]["date"] = h_element.xpath(quote_tweet_date)[0].attrib['datetime']
		tweet["quote_tweet"]["text"] = ''.join(x.text_content() for x in h_element.xpath(quote_tweet_text))
		
		tweet["quote_tweet"]["has_images"] = len(h_element.xpath(quote_tweet_image_links)) > 0

		if tweet["quote_tweet"]["has_images"]:
			tweet["quote_tweet"]["images"] = []
			for i in h_element.xpath(quote_tweet_image_links):
				try:
					tweet["quote_tweet"]["images"].append(i.attrib['src'])
				except:
					tweet["quote_tweet"]["images"].append("error")


		tweet["quote_tweet"]["reply_info"] = text_content_macro(h_element,[replying_to_banner,replying_to_banner_2])

	return tweet


#return json.dumps(iterate_tweets(tweet_elements),indent=4,ensure_ascii=False).encode('utf-8')
def get_tweets(html_string):
	return iterate_tweets(html.fromstring(html_string).xpath(tweet_dom_array))

def get_bio(html_string):
	return serializeBio(html.fromstring(html_string))

if __name__ == "__main__":
	if len(sys.argv) != 3:
		raise Exception("err input")
	if sys.argv[1] == "url":
		print("cant do direct url (javascript)")
		# r = requests.get(sys.argv[2])
		# open("outh.html","w+",encoding="utf-8").write(r.text)
		# tree = html.fromstring(r.text).xpath(tweet_dom_array)
		# open("out.json","w+",encoding="utf-8").write(json.dumps(iterate_tweets(tree),indent=4))
	if sys.argv[1] == "path":
		f = open(sys.argv[2],"r",encoding="utf-8").read()
		tree = html.fromstring(f).xpath(tweet_dom_array)
		open("out.json","wb").write(json.dumps(iterate_tweets(tree),indent=4,ensure_ascii=False).encode('utf-8'))
	else:
		raise Exception("err input")

