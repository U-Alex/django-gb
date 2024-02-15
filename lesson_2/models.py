from django.db import models


class Coin(models.Model):
    side = models.CharField(max_length=5)
    timestamp = models.DateTimeField(auto_now=True)

    @staticmethod
    def get_last_n_flip(n):
        flips = Coin.objects.all().order_by('-pk')[:n]
        result = {}
        for flip in flips:
            if result.get(flip.side):
                result[flip.side] += 1
            else:
                result[flip.side] = 1

        return result


