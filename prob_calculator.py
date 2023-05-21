import copy
import random
# Consider using the modules imported above.

class Hat:

    def __init__(self, **kwargs):
        self.contents = []
        for key, value in kwargs.items():
            for i in range(0, value):
                self.contents.append(key)

    def draw(self, nballs):
        total_balls = len(self.contents)
        balls_removed = []

        try:
            balls = random.sample(self.contents, nballs)
        except:
            balls = copy.deepcopy(self.contents)
        
        for ball in balls:
            self.contents.remove(ball)
        """
        if nballs < total_balls:
            for i in range(0, nballs):
                total_balls = len(self.contents)
                remove_i = random.randint(0, total_balls - 1)
                balls_removed.append(self.contents[remove_i])
                del self.contents[remove_i]
        """        
        return balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    """
    1. Get the balls removed
    2. 
    """

    M = 0
    for i in range(0, num_experiments):
        hat_copy = copy.deepcopy(hat)
        balls_removed = hat_copy.draw(num_balls_drawn)
        test = True

        for values, key in expected_balls.items():
            ntest = balls_removed.count(values)
            
            if ntest < key:
                test = False
                break
        
        if test:
            M += 1
           
    
    
    return M/num_experiments


hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                  expected_balls={"red":2,"green":1},
                  num_balls_drawn=5,
                  num_experiments=2000)