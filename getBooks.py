import requests
import BeautifulSoup

#Script based off of https://www.reddit.com/r/learnpython/comments/1y1kit/my_script_to_download_top_100_books_from_project/

def dowload_top_100():
    '''This script will download Top 100 books of last 30 days from Project 
    Gutenberg and saves them with appropriate file name'''
    base_url = 'http://sailor.gutenberg.lib.md.us/  '#base_url = 'http://www.gutenberg.myebook.bg/'
    response = requests.get('http://www.gutenberg.org/browse/scores/top')
    soup = BeautifulSoup(response.text)
    h_tag = soup.find(id='books-last30')
    ol_tag = h_tag.next_sibling.next_sibling
    for a_tag in ol_tag.find_all('a'):
        m = re.match(r'(.*)(\(\d+\))', a_tag.text)
        book_name = m.group(1).strip()
        m = re.match(r'/ebooks/(\d+)', a_tag.get('href'))
        book_id = m.group(1)
        # ugh, I know this is ugly.
        url = base_url + '/'.join(list(book_id[:-1])) + '/' + book_id + '/' + book_id + '.txt'
        r = requests.get(url)
        if r.status_code == requests.codes.ok:
            # print 'Downloaded... ', file_name
            with open(file_name, 'w') as f:
                f.write(r.text.encode('UTF-8'))
        else:
            print 'Failed for ', book_id