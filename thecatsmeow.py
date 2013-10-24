#--
#
# Description: Thecatsmeow
#
#       Authors:
#               Taylor Pennington @ CORE Security Technologies, CORE SDI Inc.
#               Level @ CORE Security Technologies, CORE SDI Inc.
#
#       Use: python thecatsmeow.py password_list.txt 10
#	     This will provide the top ten most occuring hashcat masks
#            in the password list. Thecatsmeow does not process UTF-8.
#
#THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
#AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
#WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. 
#IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, 
#INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT 
#NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR 
#PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, 
#WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) 
#ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE 
#POSSIBILITY OF SUCH DAMAGE.
#
#--
from collections import Counter
from sys import argv

class Hashcat:
	def __init__(self):
		self.special = '!@#$%^&*()-=_+[]|;:",./<>?'
		self.alpha = 'QWERTYUIOPASDFGHJKLZCVBNMqwertyuiopasdfghjklzxcvbnm'
		self.numeric = '0123456789'
		return
	def pass_to_hashcat(self,words):
		out = []
		for word in words:
			length,pos,wordInfo = len(words),0,{}
			for letter in word:
				if (letter in self.special): 
					wordInfo[pos] = "?s"
				elif (letter in self.alpha):
					if (letter.isupper() == True):
						wordInfo[pos] = "?u"
					else:
						wordInfo[pos] = "?l"
				elif (letter in self.numeric):
					wordInfo[pos] = "?d"
				pos+=1
			out.append(wordInfo)
		return out

def main():
	fp = open(argv[0],'r')
	words = fp.read()
	fp.close()
	words.sort(key=len),sorted = []
	for word in Hashcat().pass_to_hashcat(words):
		value = ""
		for key in word.iterkeys():
			value+=word[key]
		sorted.append(value)
	for word in Counter(sorted).most_common(argv[2]):
		print word[0],word[1]

	return

if __name__=="__main__":
	main()
