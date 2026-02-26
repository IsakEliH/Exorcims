class Luhn:
    def __init__(self, card_num:str):
        self.card_num = card_num.replace(" ", "")

    def valid(self) -> bool:
        if len(self.card_num) <= 1:
            return False
        
        for char in self.card_num:
            try:
                char = int(char)
            except:
                return False
        
        final_list = [int(x) for x in self.card_num]

        for i in range(len(self.card_num) -2, -1, -2):
            final_list[i] = final_list[i] * 2
            if final_list[i] > 9:
                final_list[i] = final_list[i] - 9

        the_sum = sum(final_list)

        if the_sum % 10 == 0:
            return True
        else: return False
