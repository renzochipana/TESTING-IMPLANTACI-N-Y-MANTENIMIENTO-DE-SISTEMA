import array
import random
class Queue:
	def __init__(self,size_max):
		assert size_max > 0
		self.max = size_max
		self.head = 0
		self.tail = 0
		self.size = 0
		self.data = array.array('i', range(size_max))

	def empty(self):
		return self.size == 0

	def full(self):
		return self.size == self.max

	def enqueue(self,x):
		if self.size == self.max:
			return False
		self.data[self.tail] = x
		self.size += 1
		self.tail += 1
		if self.tail == self.max:
			self.tail = 0
		return True

	def dequeue(self):
		if self.size == 0:
			return None
		x = self.data[self.head]
		self.size -= 1
		self.head += 1
		if self.head == self.max:
			self.head = 0
		return x

def test1():
	q = Queue(2)
	res = q.empty()
	if not res:
		print("test1 NOT ok")
		return
	res = q.enqueue(10)
	if not res:
		print("test1 NOT ok")
		return
	res = q.enqueue(11)
	if not res:
		print("test1 NOT ok")
		return
	x = q.dequeue()
	if x != 10:
		print("test1 NOT ok")
		return
	x = q.dequeue()
	if x != 11:
		print("test1 NOT ok")
		return
	res = q.empty()
	if not res:
		print("test1 NOT ok")
		return
	print("test1 OK")

def test2():  #prueba con una cola llena y vacia
    q = Queue(2)
    if not q.empty():
        print("test2 NOT ok: la cola no está vacia al inicio")
        return
    if not q.enqueue(10):
        print("test2 NOT ok: no se pudo encolar 10")
        return
    if not q.enqueue(11):
        print("test2 NOT ok: no se pudo encolar 11")
        return
    if not q.full():    # Ahora debe estar llena
        print("test2 NOT ok: la cola no está llena después de 2 elementos")
        return
    # Intentamos encolar uno más (no debería poder)
    if q.enqueue(12):  # si devuelve True, está mal
        print("test2 NOT ok: se encoló un elemento extra en cola llena")
        return
    print("test2 OK")
    
def test3():   #prueba con una cola que usa la vuelta a 0 de sus head y tail cuando encola y decola
    q = Queue(2)
    q.enqueue(1)
    q.enqueue(2)
    q.dequeue()
    q.enqueue(3)  # Esto hace que tail vuelva a 0 porque es circular
    if q.dequeue() != 2:
        print("test3 NOT ok: no se desencoló correctamente 2")
        return
    if q.dequeue() != 3:
        print("test3 NOT ok: no se desencoló correctamente 3")
        return
    if not q.empty():
        print("test3 NOT ok: la cola debería estar vacía")
        return
    print("test3 OK")
    
    
def test4():
    q = Queue(2)
    res = q.enqueue(-5)
    if not res:
        print("test4 NOT ok: no se pudo encolar -5")
        return
    res = q.enqueue(-10)
    if not res:
        print("test4 NOT ok: no se pudo encolar -10")
        return
    res = q.enqueue(-15)
    if res:
        print("test4 NOT ok: se encoló -15 pero la cola ya estaba llena")
        return
    x = q.dequeue()
    if x != -5:
        print("test4 NOT ok: se esperaba -5 y se obtuvo", x)
        return
    x = q.dequeue()
    if x != -10:
        print("test4 NOT ok: se esperaba -10 y se obtuvo", x)
        return
    if not q.empty():
        print("test4 NOT ok: la cola debería estar vacía")
        return
    print("test4 OK")


test1()
test2()
test3()
test4()

