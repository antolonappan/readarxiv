readarxiv(){
      cd /Users/anto/Arxiv
      python arxiv.py
      say -f .arxiv.txt
      rm .arxiv.txt
      cd
