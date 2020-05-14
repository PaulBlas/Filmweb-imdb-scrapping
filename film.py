import io

class Film:
    fw_scores = {}
    imdb_scores = {}
    fw_imdb_scores = {}

    def merge(self):
        for k, v in self.fw_scores.items():
            if k in self.imdb_scores:
                self.fw_imdb_scores[k] = round(((self.imdb_scores[k]+v)/2), 2)


    def sort(self):
        self.fw_imdb_scores = {k: v for k, v in sorted(self.fw_imdb_scores.items(), key=lambda item: item[1], reverse=True)}
        self.imdb_scores = {k: v for k, v in sorted(self.imdb_scores.items(), key=lambda item: item[1], reverse=True)}
        self.fw_scores = {k: v for k, v in sorted(self.fw_scores.items(), key=lambda item: item[1], reverse=True)}


    def fw_save_to_txt(self):
        with io.open('FW_ocena_popularność.txt', 'w', encoding='utf8') as wf:
            wf.write('--FILMWEB NAJLEPSZE FILMY OCENA/POPULARNOSC\n')
            for k, v in self.fw_scores.items():
                wf.write(f'{k}: {v}\n')

    def imdb_save_to_txt(self):
        with io.open('Imdb_ocena_popularność.txt', 'w', encoding='utf8') as wf:
            wf.write('--IMDB NAJLEPSZE FILMY OCENA/POPULARNOSC\n')
            for k, v in self.imdb_scores.items():
                wf.write(f'{k}: {v}\n')

    def all_save_to_txt(self):
        with io.open('RANKING WSZECHCZASÓW.txt', 'w', encoding='utf8') as wf:
            i = 1
            wf.write('--RANKING WSZECHCZASÓW\n')
            for k, v in self.fw_imdb_scores.items():
                wf.write(f'{i}. {k}: {v}\n')
                i+=1





