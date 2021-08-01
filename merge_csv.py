import csv

headers = []
all_movies = []
all_movies_links = []

with open('movies.csv', encoding='utf8') as f:
    reader = csv.reader(f)
    data = list(reader)
    all_movies = data[1:]
    headers = data[0]

headers.append("poster_link")

with open('final.csv', "a+") as f:
    writer = csv.writer(f)
    writer.writerow(headers)

with open("movie_links.csv", encoding="utf8") as f:
    reader = csv.reader(f)
    data = list(reader)
    all_movies_links = data[1:]

for movieItems in all_movies:
    poster_found = any(movieItems[9] in movieLinkItems for movieLinkItems in all_movies_links)
    
    if poster_found:
        for movieLinkItem in all_movies_links:
            if movieItems[9] == movieLinkItem[0]:
                movieItems.append(movieLinkItem[1])
                if len(movieItems) == 28:
                    with open("final.csv", "a+") as f:
                        writer = csv.writer(f)
                        writer.writerow(headers)
#                         writer.writerows(movieItems)

            