from django.db import models


class Stadium(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Block(models.Model):
    stadium = models.ForeignKey(Stadium)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_seat_list(self):
        seat_dict = { (seat.row, seat.col):seat for seat in self.seat_set.all() }
        max_row = max(row for (row, col) in seat_dict.keys())
        max_col = max(col for (row, col) in seat_dict.keys())
        seat_list = []
        for row_idx in range(max_row):
            row_list = []
            for col_idx in range(max_col):
                key = (row_idx, col_idx)
                seat = seat_dict.get(key, None)
                row_list.append((row_idx, col_idx, seat))
            seat_list.append(row_list)
        return seat_list


class Seat(models.Model):
    block = models.ForeignKey(Block)
    row = models.PositiveIntegerField()
    col = models.PositiveIntegerField()
    photo = models.ImageField()
    is_blind = models.BooleanField(default=False)

    def __str__(self):
        return '{}행 {}열'.format(self.row, self.col)

    class Meta:
        unique_together = [
            ('block', 'row', 'col'),
        ]

