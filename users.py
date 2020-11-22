class users:
    """
    class that show user accounts
    """
    user_list = []

    def __init__(self,user_name,user_password):

        self.first_name = user_name
        self.last_name = user_password
        
    def save_users(self):

        """
        save users credentials
        """

        users.user_list.append(self)

       
    

