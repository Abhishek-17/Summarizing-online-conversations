	



#Basic Description


Summarization has emerged as an increasingly useful approach to tackle the problem of information overload. Extracting information from online conversations can be of very good commercial and educational value. But majority of this information is present as noisy unstructured text making traditional document summarization techniques difficult to apply. In this project, we propose a novel approach to address the problem of conversation summarization. We develop an automatic text summarizer which extracts sentences from the email conversations to form a summary. Our approach consists of three phases. In the first phase, we prepare the dataset for usage by correcting spellings and segmenting the text. In the second phase, we represent each sentence by a set of predefined features. Finally, in the third phase we use a machine learning algorithm to train the summarizer on the set of feature vectors. We also a developed an interface which takes as input the document to be saummarized and retuns an extractive summary.



#How to run summarizer from Commandline


python summarize.py 'path of test chunk'



#How to run summarizer from UI


1. Copy all the files/codes to the /var/www folder or your own htdocs folder of the apache server.
2. Run http://localhost/index.php (or path to the index.php)
2. Upload the sample test data file which has one thread in the below given format.
3. Optionally upload the summary file to get precision and recall of the summarizer
4. The system would show the important sentences (summary) and their corresponding sentence ids on the web page



#Instructions about test and summary-id files 


1.	The sample test data file should have content in following format (not correctly shown here. download this file and open it in text editor)-

<thread>
    <name>Try Unsubscribing&amp;ndash;&amp;ndash;You Can't</name>
    <listno>107-16164699</listno>
    <DOC>
      <Received>Tue Nov 12 13:26:50 -0800 1996</Received>
      <From>Rob Wood &lt;rwood@hypergold.com&gt;</From>
      <To>www-font@w3.org</To>
      <Subject>Try Unsubscribing&amp;ndash;&amp;ndash;You Can't</Subject>
      <Text>
        <Sent id="1.1">Chris Lilley, Brian Stell and others have been discussing the rash of irate, &amp;quot;get me off this list&amp;quot; mesages the listserv has received, lately. </Sent>
        <Sent id="1.2">Well, folks: YOU CAN'T UNSUBSCRIBE FROM THIS LIST! </Sent>
        <Sent id="1.3">I've tried for 2 months to get off this list, I've followed the rules, I've tried variations of the theme, looking for some hidden code--all to no avail. </Sent>
        <Sent id="1.4">So, the last resort of those who have tried everything else is to post to the list they want to be rid of. </Sent>
        <Sent id="1.5">It's irony, but it's a fact. </Sent>
      </Text>
    </DOC>
    <DOC>
      <Received>Tue Nov 12 13:37:04 -0800 1996</Received>
      <From>Kimberly Haeger &lt;kimh@netscape.com&gt;</From>
      <To>www-font@w3.org</To>
      <Subject>Re: Try Unsubscribing&amp;ndash;&amp;ndash;You Can't</Subject>
      <Text>
        <Sent id="2.1">Well, that explains a lot! </Sent>
        <Sent id="2.2">I've been trying for awhile too, and I can't seem to get off. </Sent>
        <Sent id="2.3">Please! </Sent>
      </Text>
    </DOC>
  </thread>


2.	The summary file has the ids of sentences from the test file which should be in the summary of the thread and is used to find precision and recall. It should be in the following format (1 sentence id per line)

	1.2
	1.3
	2.1
	2.2
	2.3



#Files/Folders and their Descriptions


1. annotation.xml: tagged xml corpus

2. centroid_coherence.py: calculates the centroid-coherence of the sentences in the thread

3. createTestDataset.py: generates the test dasta from the test xml file in the format suitable to feed to the nltk naive bayes classifier.

4. css.css : css file for the UI index.php

5. images: folder containing images for the UI

6. index.php: UI for using the summarizer

7. is_question.py: generates the Is_question feature i.e. identifies the questions in the email thread.

8. length_pos.py: generates  the normalized length and position of the sentences of the thread.

9. merge.py: Takes various featues from other files like tfidf, tfisf, sentence length, sentence position , centriod coherence etc and merges them so as to generate the data that can be usd with the nltk classifier. 

10. precision_racall.py: calculates the precision recall when the user gives the imporatant sentence ids through UI.

11. splitted: folder containing splitted BC3 training corpus. Each file represents an individual thread.

12. summarize.py: The main file. Takes the path of file to be tagged and path of splitted training threads and generates  summary using them.

13. testSplitted: Contains the test file which to be tagged

14. tf_idf.py: calculates the tf-idf of the sentences.

15. tf_isf.py: calculates the tf-idf of the sentences.

16. title_simm.py: calculates the title similarity scre for sentences in the thread.

17. SummaryThreads : folder havin tagged data

#Requirements/Dependencies


1. Apache server (for GUI index.php only )
2. python 2.7 
3. NLTK library   ( instructions to install in link : http://www.nltk.org/install.html )
