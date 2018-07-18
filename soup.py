#Library and Header File inclusion
import urllib.request
import xlsxwriter
import sqlite3
from bs4 import BeautifulSoup

#Connecting to database

conn=sqlite3.connect("python_project.db")
#conn.execute('''CREATE TABLE SCRAPPING(LIST_OF_WORDS TEXT, DENSITY_OF_WORDS FLOAT);''')

#Initialize Variables
j=0
i=0
sheet_count=0

#Accessing File containing URLs

fileopen=open("E:/URL.txt","r")
URL=fileopen.read().split()
list_of_URL=list(URL)
print(list_of_URL)

#Initializing Excel Workbook

workbook=xlsxwriter.Workbook('e://sheet.xlsx')

#Iterate through Each URLs

for j in list_of_URL:
    req=urllib.request.Request(j)
    page=urllib.request.urlopen(req)
    soup=BeautifulSoup(page,"html.parser")
    print(soup.title.string)

    #Extracting specific content from URL
    
    for script in soup(["script","style"]):
        script.extract()
    text=soup.get_text()
    print(text)
    lines=(line.strip() for line in text.lower().split())
    for line in lines:
        print(line)
    print("\n Success")

    #Open file containing stop words to be removed from the extracted content
    
    fopen=open("E:/stop_words.txt","r")
    stop_words=fopen.read().split()
    stop_words_set=set(stop_words)
    fopen.close()

    #Initialize dictionary and lists for frequency, list of words and density
    
    count={}
    density=[]
    word_list=[]
    total=len(text)

    #Adding list of words after removing stop words from scrapped content
    
    for word in text.lower().split():
        if word not in stop_words_set:
            if word not in count:
                count[word]=1
            else:
                count[word]+=1

    #Find Density for each word
                
    for i in count.keys():
        density.append((count[i]/total)*100)
        word_list.append((i,(count[i]/total)*100))
    print(count)

    #Extracting list of words and count of respective word from the dictionary
    
    list_of_words=count.keys()  
    word_count=count.values()

    #Creating sheets for each URLs
    
    sheet_count=sheet_count+1
    sheet="sheet%s"%i
    worksheet=workbook.add_worksheet()

    #Adding List Of words to the Worksheet
    
    worksheet.write("A1","Word list")
    worksheet.set_column('A:A', 20)
    row=1
    col=0
    worksheet.write_column(row,col,list_of_words)

    #Adding count of each word to the Worksheet
    
    worksheet.write("B1","Word Count")
    worksheet.set_column('B:B',20)
    row=1
    col=1
    worksheet.write_column(row,col,word_count)

    #Adding density of each word to the Worksheet
    
    worksheet.write("C1","Density of words")
    worksheet.set_column('C:C',20)
    row=1
    col=2
    worksheet.write_column(row,col,density)

    #Creating a chart for each Worksheet
    
    chart=workbook.add_chart({'type':'bar'})
    chart.add_series({'values':'=Sheet%d!$C$1:$C$30'%sheet_count})
    worksheet.insert_chart('G5',chart)

    #Accessing the Database
    
    print("Connecting to DB...")
    conn.commit()
    c=conn.cursor()

    #Inserting Data into the Database
    
    c.executemany('''INSERT INTO SCRAPPING(LIST_OF_WORDS, DENSITY_OF_WORDS) VALUES(?,?)''' ,(word_list))

    #Displaying the data entered in the database
    
    db=c.execute('''SELECT * FROM SCRAPPING''')
    for data in db:
        print(data)
    conn.commit()

#Closing the Database connection

conn.close()

#Closing the Workbook

workbook.close()
print("\n Scrapping was Successful and Scrapped data is stored in Excel and Database using Python")
