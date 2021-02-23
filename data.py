from bs4 import BeautifulSoup
import requests
def scrape_poll_data():
    URL = 'https://projects.fivethirtyeight.com/polls/president-general/'
    html_data = requests.get(URL)

    soup = BeautifulSoup(html_data.content, 'html.parser')
    rows = soup.find_all(class_='visible-row')

    pollster_data_array=[]

    for r in rows:
        date = r.find(class_='date-wrapper').text 
        #print(date,'\n')

        pollster = r.find(class_='pollster-container')
        pollster_text = pollster.find_all("a")[-1].text
        #print(pollster_text,"\n")

        sample_size = r.find(class_='sample').text

        leader = r.find(class_='leader').text

        net = r.find(class_='net').text

        #print(sample_size,leader, net, "\n")

        answers = r.find_all(class_="answer")
        values = r.find_all(class_="value")
        #print(answers)
        if len(values) == 1:
            next_row = r.findNext("tr")
            value = next_row.find(class_="value")
            answer = next_row.find(class_= "answer")
            
            answers.append(answer)
            values.append(value)
        #print(answers)
        first_person = answers[0].text
        #print(first_person)
        seccond_person = answers[1].text
        #print(seccond_person)

        first_value = values[0].find(class_="heat-map").text
        seccond_value = values[1].find(class_="heat-map").text

        pollster_data = {
            "date": date,
            "pollster_name": pollster_text,
            "sample_size": sample_size,
            "leader": leader,
            "net":net,
            "first_person": first_person,
            "first_value": first_value,
            "seccond_person": seccond_person,
            "seccond_value": seccond_value
        }
        pollster_data_array.append(pollster_data)
        
    return pollster_data_array

 