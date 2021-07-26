# Django
from django.views import View
from django.http import HttpResponse, JsonResponse
from .models import PasswdFinder

# Utilities
import os

class PasswdFinderView(View):
    def get(self, request):
        # Get path
        module_dir = os.path.dirname(__file__)
        self.file_path = module_dir + '/resources/keylog.txt'

        # Get Password
        passwd = self.get_passwd()

        # Create Record
        passwd_obj = PasswdFinder.objects.create(passwd=passwd)
        data = PasswdFinder.objects.filter(pk=passwd_obj.id).values()
        return JsonResponse(list(data), safe=False)

    def get_passwd(self):
        """
          The following algorithm takes a series of N-digit samples
          and try to calculate the shortest password that corresponds to said
          set of sequences, through a series of iterations.
          In the specific case of the problem, the samples consist of
          3 digits.
          Returns:
              password: Password calculated by the algorithm
        """
        # Get dataset
        data_file = open(self.file_path, mode='r').readlines()
        dataset = [data.strip() for data in data_file]
        dataset = set(dataset)

        password = ""

        for data in dataset:
            # Init Values
            position_number_current, position_number_old = 0, 0
            for digit in data:
                # The digit  exist in the password
                if digit in password:
                    position_number_current = password.find(digit)
                    # The digit  exists  in the password and IT is in the correct position
                    if (position_number_current > position_number_old):
                        pass
                    # The digit  exists  in the password but needs to be relocated  for the present sequence
                    else:
                        password = password[:position_number_current] + \
                                   password[position_number_current+1:position_number_old+1] + \
                                   digit + \
                                   password[position_number_old+1:]
                # The digit  doesnt exist in the password yet.  IT is adds to the last position
                else:
                    password += digit
                    position_number_current = len(password)
                position_number_old = position_number_current
        return password