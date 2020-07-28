{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1 2 3 4]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "a = np.array([1,2,3,4])\n",
    "print(a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 2, 3, 4, 1, 2, 3, 4]\n"
     ]
    }
   ],
   "source": [
    "a=[1,2,3,4] #리스트\n",
    "b=[1,2,3,4]\n",
    "print(a+b) #리스트가 겨결합됨"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[2 4 6 8]\n"
     ]
    }
   ],
   "source": [
    "a=np.array([1,2,3,4]) #array:배열(1차원), 행렬(2차원), 텐서(3차원 이상)\n",
    "b=np.array([1,2,3,4])\n",
    "print(a+b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1.4 2.4 3.3 4.2]\n",
      "[0.6 1.6 2.7 3.8]\n",
      "[0.4 0.8 0.9 0.8]\n",
      "[ 2.5  5.  10.  20. ]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "a=np.array([1, 2, 3, 4])\n",
    "b=np.array([.4, .4, .3, .2])\n",
    "print(a+b)\n",
    "print(a-b)\n",
    "print(a*b)\n",
    "print(a/b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[ 6  8]\n",
      " [10 12]]\n",
      "[[ 5 12]\n",
      " [21 32]]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "A = np.array([[1,2],[3,4]]) # [1,2]\n",
    "                            # [3,4] --2행*2열 행렬\n",
    "B = np.array([[5,6],[7,8]])\n",
    "print(A+B)\n",
    "print(A*B)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[ 6  8]\n",
      " [10 12]]\n",
      "[[ 5 12]\n",
      " [21 32]]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "A = np.array([[1,2],[3,4]]) # [1,2]\n",
    "                            # [3,4] --2행*2열 행렬\n",
    "B = np.array([[5,6],[7,8]])\n",
    "C = np.array([[1,2],[3,4],[5,6],[7,8]]) # 텐서\n",
    "print(A+B)\n",
    "print(A*B)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[ 7 10]\n",
      " [15 22]]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "A = np.array([[1,2],[3,4]])                           \n",
    "B = np.array([[1,2],[3,4]])\n",
    "print(np.dot(A,B)) # dot 행렬곱하는명령어 "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[ 1  4]\n",
      " [ 9 16]]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "A = np.array([[1,2],[3,4]])                           \n",
    "B = np.array([[1,2],[3,4]])\n",
    "print(A*B) # 행렬요소의 곱"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0 1 2]\n",
      "[5 6 7]\n",
      "[[1. 1. 1.]\n",
      " [1. 1. 1.]\n",
      " [1. 1. 1.]]\n",
      "[[1. 2. 3.]\n",
      " [1. 2. 3.]\n",
      " [1. 2. 3.]]\n",
      "[[0]\n",
      " [1]\n",
      " [2]]\n",
      "[[0 1 2]\n",
      " [1 2 3]\n",
      " [2 3 4]]\n"
     ]
    }
   ],
   "source": [
    "A=np.arange(3)\n",
    "B=np.arange(3)+5\n",
    "C=np.ones((3,3))\n",
    "D=np.ones((3,3))+ np.arange(3)\n",
    "E=np.arange(3).reshape((3,1))\n",
    "F=np.arange(3).reshape((3,1))+np.arange(3)\n",
    "print(A)\n",
    "print(B)\n",
    "print(C)\n",
    "print(D)\n",
    "print(E)\n",
    "print(F)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.7.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
