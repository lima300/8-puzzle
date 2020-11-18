import time
from game import Board

class App:
    """
    Representa a aplicação CLI.
    """
    def __init__(self, start_matrix, end_matrix):
        self.board = Board(start_matrix, end_matrix)
        self.solution = None
    
    def solve(self):
        time_limit = float(input('Entre com o tempo limite (segundos) para resolução do problema: '))
        time_start = time.time()       
        
        print('Solving...')
        print()

        self.solution = self.board.deepening_search(time_start=time_start, time_limit=time_limit)

        if self.solution is None:
            print('Tempo de busca em profundidade se esgotando. Iniciando heurística...\n')
            time_start = time.time()
            self.solution = self.board.solve()
            time_end = time.time()
            print('Tempo de execução da busca A*: %0.10fs' % (time_end-time_start))
        else:
            time_end = time.time()
            print('Tempo de execução da busca em profundidade: %0.10fs' % (time_end-time_start))
        
       
    
    def display_solution(self):
        print('# Initial #'.center(13))
        print()
        print(self.board)
        print()
        
        for i, pos in enumerate(self.solution):
            input('Press ENTER to continue')
            print()
            self.board.move(pos)            
            print('# {} #'.format(i+1).center(13))
            print()
            print(self.board)
            print()