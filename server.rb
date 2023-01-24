require "sinatra"
require_relative "./ask/chat_gpt.rb"

get "/ask/?" do
  content_type :json

  OpenAI::ChatGPT.new(params["question"]).answer
end
