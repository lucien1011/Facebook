
import facebook
import requests
from option import parser

#____________________________________________________________________________||

parser.add_argument('--message', action = 'store', dest = 'message', help = 'message to be sent')

#____________________________________________________________________________||

args = parser.parse_args()

#____________________________________________________________________________||

token = args.token
wallMessage = args.message

#____________________________________________________________________________||

# https://developers.facebook.com/tools/explorer/
access_token = token
user = "me"

graph = facebook.GraphAPI(access_token)
profile = graph.get_object(user)
posts = graph.get_connections(user, 'friends')

graph.put_object( user , "feed", message = wallMessage )
