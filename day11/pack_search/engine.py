from selenium_search import WebSearcher

web=WebSearcher()


class SearchFromComandLine():
    # Purpose of the class is to allow user to search information from comand line direcly
    def InitializingOfTheSearch(self):
        portal_name = "https://"+input("Please put name of site")
        user_input_from_the_line = input(
            "Please parse name of the web search element")
        user_input_search_criteria = input("Pleae prpvide search criteria")
        web.search_on_page(
            portal_name, user_input_from_the_line, user_input_search_criteria)
            
cmd = SearchFromComandLine()
cmd.InitializingOfTheSearch()