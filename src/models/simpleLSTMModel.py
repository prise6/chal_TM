from src.models.AbstractModel import AbstractModel
from keras.models import Sequential, load_model
from keras.layers import Dense, Activation, Embedding, Dropout, TimeDistributed
from keras.layers import LSTM


class simpleLSTMModel(AbstractModel):

	def __init__(self, save_directory, vocabulary_size, lstm_hidden_size, batch_input_shape):

		super().__init__(save_directory)

		self.vocabulary_size = vocabulary_size
		self.lstm_hidden_size = lstm_hidden_size
		self.batch_input_shape = batch_input_shape
		self.build_model()


	def build_model(self):

		model = Sequential()
		model.add(Embedding(input_dim = self.vocabulary_size, output_dim = self.lstm_hidden_size, batch_input_shape = self.batch_input_shape))
		model.add(LSTM(self.lstm_hidden_size, return_sequences=True))
		model.add(LSTM(self.lstm_hidden_size, return_sequences=True))
		model.add(Dropout(0.5))
		model.add(TimeDistributed(Dense(self.vocabulary_size)))
		model.add(Activation('softmax'))

		model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['categorical_accuracy'])

		self.model = model

		return self.model








