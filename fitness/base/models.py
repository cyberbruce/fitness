from django.db import models
import re

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class PrettyModelMixIn:
    def __str__(self):
        fl = []
        for field_name in self._meta.get_fields():              
            last_seg = re.split(r'\.', str(field_name))[-1] 
            try:          
                fl.append(f"     {last_seg}: {bcolors.OKGREEN}{getattr(self, str(last_seg))}{bcolors.ENDC}")
            except:
                pass
        return "\n" + "\n".join(fl) + "\n"

class FitnessModel(PrettyModelMixIn, models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
