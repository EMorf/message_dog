import pickle


class TriviaAnswer(): 
	
	def __init__(self, name):
		self.name = name
		try:
			with open('obj/' + name + '.pkl', 'rb') as f:
				self.answers = pickle.load(f)
		except Exception as e:
			self.answers = {}
			print(e)
			
	def save_data(self):
		with open('obj/'+ self.name + '.pkl', 'wb') as f:
			pickle.dump(self.answers, f, pickle.HIGHEST_PROTOCOL)
			
	def set_data(self, question, answer):
		try:
			if question not in self.answers:
				self.answers[question] = answer
				self.save_data()
				return True
		except:
			return False
		
	def retrieve(self, question):
		return self.answers.get(question, "")
		
if __name__ == "__main__": 
    #Run some tests, be sure to remove everything in the obj folder first
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
	
