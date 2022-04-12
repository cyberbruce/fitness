from django.db import models
import re


class bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


class PrettyModelMixIn:
    def __repr__(self):
        fl = [
            f"     {k} : {bcolors.OKGREEN}{v}{bcolors.ENDC}"
            for k, v in self.__dict__.items()
        ]
        return "\n" + f"     {self._meta.db_table}\n" + "\n".join(fl) + "\n"


class FitnessModel(PrettyModelMixIn, models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
