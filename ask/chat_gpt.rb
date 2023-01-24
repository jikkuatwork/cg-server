require "dotenv"

Dotenv.load

module OpenAI
  class ChatGPT
    attr_reader :question

    def initialize(question)
      @question = question
      open(ENV["SWAP_FILE"], "w").write(question)
    end

    def answer
      while true
        answer = read_and_clear(ENV["ANSWER_FILE"]).strip

        unless (answer.empty?)
          return { "answer": answer }.to_json
        end
      end
    end

    def read_and_clear(file)
      answer = open(file, "r").read
      open(file, "w").write("")

      answer
    end
  end
end
