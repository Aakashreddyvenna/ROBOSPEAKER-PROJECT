{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d4680341",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Welcome to robospeaker 1.1 created by aakash\n",
      "enter the words to speakaakash\n",
      "enter the words to speakok\n",
      "enter the words to speakhello\n"
     ]
    }
   ],
   "source": [
    "import os\n",
    "if __name__ ==  '__main__' :\n",
    "    print(\"Welcome to robospeaker 1.1 created by aakash\")\n",
    "    while True:\n",
    "        x=input(\"enter the words to speak\")\n",
    "        if x == 1:\n",
    "            os.system(\"bye bye\")\n",
    "            break\n",
    "        command= f\"say {x}\"\n",
    "        os.system(command)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
