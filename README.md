# aptoide
##Solution Description
  My solution is based on two major pacakges 
  Django 1.11    https://docs.djangoproject.com/en/2.2/releases/1.11/
  django-selectable  https://pypi.org/project/django-selectable/0.1.2/
  Django as the web frame work and django_selectable for the  Autocomplete filtering and API.

  Installing these packages should be enough. However there is a requirements.txt that contains the packages requied as well

  This approach ensures that the coding required is minimal as requested.

  The solution loads the test data into a list data structure at initiation(that is when the  webserver in satrting up as requested in the document. The list is passed to the django-selectable where there filtering and API access is managed an the lookup.py file. On the front end, a filtered list is presented below the shearch field and the whole list may be viewed from the drop down button

  A form object(subclassing Djongo's forms.Form) is created with only one  field(presumably sufficient to test) that instantiates the AutocompleteSelectField class of Django-Selectable where we can test the filtering.

  A very basic view publishes the form object in a very basic django template named 'Aptoide.html'

  To run the application, Access to the internet wil be required to load jquery/jquery UI files from CDNs.
  The Application can be initiated using the django test server by using the Manage.py runserver command.
  After thsi is done, the testing page will be available at 
  localhost:<port_no>/aptoide/my-view/
  http://localhost:1234/aptoide/my-view asumming the port is 1234
  An the API at
  http://localhost:1234/selectable/aptoide-mylookup/?term=f

  Assuming a search string 'f'.

#Testing.


  Minimal Units testing was done 
  To confirm that there the file(s) were loading and also the length of the list,
  To confirm that lenght of the list in memeory is equal to that of the file intended
  to confirm the filtering result was correct
  
