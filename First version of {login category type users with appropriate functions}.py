                    #OLD VERSION


class user:                                            # Decorator login  for four classes
    def init(self):
        self.login = input('login:')
        self.password = input('password:')
    def copy(self):
        return copy.deepcopy(self)
    def info(self):
        return self.dict
    def action1_for_user_action1(self):
        return f'login is {self.login}'
    def action2_for_user_action1(self):
        #print(sys.getsizeof(self))
        return f'password is {self.login}'
    def info(self):
        return self.dict
    
class admin:                                             
    def init(self):
        self.login = input('login:')
        self.password = input('password:')
        self.is_admin = True
    def copy(self):
        return copy.deepcopy(self)
    def info(self):
        return self.dict

class support_user:
    def init(self):
        self.login = input('login:')
        self.password = input('password:')
        self.is_support = True
    def copy(self):
        return copy.deepcopy(self)
    def info(self):
        return self.dict

class server_admin_user:
    def init(self):
        self.login = input('login:')
        self.password = input('password:')
        self.is_admin = True
        self.server_admin = True
    def copy(self):
        return copy.deepcopy(self)
    def info(self):
        return self.dict


admin_users = []
users = []
server_admin_users = []
support_users = []

def AdminLogin():
    user = admin_user()
    if not admin_users:
        admin_users.append(user)
    else:
        for db_user in users:
            if user.login == db.user.login and user.password == db.user.password:
                return True

def UserLogin():
    user = user()
    if not users:
        users.append(user)
    else:
        for db_user in users:
            if user.login == db.user.login and user.password == db.user.password:
                return True

def SupportLogin():
    user = support_user()
    if not support_users:
        support_users.append(user)
    else:
        for db_user in users:
            if user.login == db.user.login and user.password == db.user.password:
                return True


def ServerAdminUserLogin():
    user = server_admin_user()
    if not users:
        admin_users.append(user)
    else:
        for db_user in users:
            if user.login == db.user.login and user.password == db.user.password:
                return True

def user_action1(user):
    print('USER action 1')
    user.action1_for_user_action1() # Для получения логина
    user.action1_for_user_action1() # Для получения пароля
    # ---------- Тут что то будет ........
    

def user_menu(user):
    print('Hello You are admin')
    while True:
        choice = input('1 user_action 2 exit')
        if choice == '1':
            user_action1()
        if choice == '2':
            break


def admin_action1(user):
    if user.is_admin:
        print('admin action 1')
        user.info()
        
def admin_action2(user):
    if user.is_admin:
        print('admin action 2')
        user.info()
        
def admin_action3(user):
    if user.is_admin:
        print('admin action 3')
        user.info()
    

def admin_menu(user):
    print('Hello You are admin')
    while True:
        choice = input('1 user_action 2 exit')
        if choice == '1':
            user_action1()
        if choice == '2':
            break



user_type = input('user,admin,support,support_admin')
if user_type == 'user':
    if UserLogin():
        print('Введите повторно логин и пароль ...')
        login = input('login:')
        password = input('password:')
        user_type = input('user,admin,support,support_admin')
        if user_type == 'user':
            for user in users:
                if user.login == login and user.password == password:
                    if type(user) == user:
                        user_menu(user)
                    if user_type == 'admin':
                        admin_menu(user)
                    if user_type == 'support':
                        pass
                    if user_type == 'support_admin':
                        pass

if user_type == 'admin':
    if AdmiLogin():
        print('Введите повторно логин и пароль ...')
        login = input('login:')
        password = input('password:')
        user_type = input('user,admin,support,support_admin')
        if user_type == 'admin':
            for user in users:
                if user.login == login and user.password == password:
                    if user_type == 'admin':
                        admin_menu(user)