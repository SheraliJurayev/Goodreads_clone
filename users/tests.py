from audioop import reverse
from django.test import TestCase
from django.contrib.auth.models import User

class RegistertarionTestCase(TestCase):
    def test_user_accaunt_is_ctrated(self):
        self.client.post(
            reverse('users:register_page') , 
             data={
            'username': 'Sh_Jurayeff' , 
            'first_name': 'Sherali' , 
            'last_name': 'Jurayev' , 
            'email': 'sheralijurayev0412@gmail.com' , 
            'password': 'Sony1122'
                                }
                        )
        user = User.objects.get(username = 'Sh_Jurayeff')

        self.assertEqual(user.first_name, 'Sherali')
        self.assertEqual(user.last_name, 'Jurayev')
        self.assertEqual(user.email, 'sheralijurayev0412@gmail.com')
        self.assertNotEqual(user.password, 'Sony1122')
        self.assertTrue(user.check_password('Sony1122'))


    def test_required_fields(self):
        response = self.client.post(
            reverse('users:register_page') , 
            data={
            'first_name': 'Sherali' , 
            'email': 'sheralijurayev0412@gmail.com'
            }
        )    

        user_count = User.objects.count()

        self.assertEqual(user_count, 0 )
        self.assertFormError(response , 'form' , 'username' , 'This field is required.')
        self.assertFormError(response , 'form' , 'password' , 'This field is required.')

    def test_invalid_email(self):
        self.client.post(
            reverse('users:register_page') , 
             data={
            'username': 'Sh_Jurayeff' , 
            'first_name': 'Sherali' , 
            'last_name': 'Jurayev' , 
            'email': 'Invalid-email' , 
            'password': 'Sony1122'
                }
                        )
            


