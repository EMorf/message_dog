import pprint
import json

class TriviaAnswer(): 
	
	def __init__(self, name):
		self.name = name
		try:
			with open('obj/' + name + '.json') as f:
				self.answers = json.load(f)
		except Exception as e:
			self.answers = {}
			print(e)
			
	def save_data(self):
		with open('obj/'+ self.name + '.json', 'w') as f:
			json.dump(self.answers, f)
			
	def set_data(self, question, answer):
		try:
			if question not in self.answers:
				self.answers[question] = answer
				self.save_data()
				return True
		except:
			return False
		
	def get_answer(self, question):
		a= (self.answers).get(question, " ")
		return a
		
	
	def data(self):
		return self.answers
		
if __name__ == "__main__": 
	ta = TriviaAnswer('stream')
	#pprint.pprint(ta.data(), compact=True)
    #Run some tests, be sure to remove everything in the obj folder first
	'''
	name = "qa-pairs"
	x = TriviaAnswer(name)
	x.set_data("2 + 2 = ?", "4")
	assert(x.retrieve("2 + 2 = ?") == '4')
	assert(x.retrieve("Hello?") == "")
	
	t_q = "This is a test generator".split(" ")
	t_a = "This is a test answer".split(" ")
	for i, j in enumerate(t_q):
		assert(x.set_data(j, t_a[i]))
	assert(x.retrieve('This') == 'This') 
	'''
