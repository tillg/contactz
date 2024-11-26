from linkedin_api import Linkedin
from linkedin_api.utils.helpers import get_id_from_urn
import logging
import os
from persistence import persist_resource
from dotenv import load_dotenv

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def scrape(username, password, public_id):
    # Authenticate using any Linkedin user account credentials
    api = Linkedin(username, password)

    # GET a profile
    logger.info(f"Getting profile for {public_id}...")
    profile = api.get_profile(public_id)
    urn_id = get_id_from_urn(profile["member_urn"])
    persist_resource("PROFILE", profile)

    # GET a profiles contact info
    logger.info(f"Getting contact info for {public_id}...")
    contact_info = api.get_profile_contact_info(public_id)
    persist_resource("CONTACTINFO", contact_info)

    logger.info(f"Getting connections for {urn_id}...")
    # connections = api.get_profile_connections(urn_id)
    # write_thing("CONNECTIONS", connections)


load_dotenv()
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
PUBLIC_ID = os.getenv("PUBLIC_ID")

if all([USERNAME, PASSWORD, PUBLIC_ID]):
    scrape(USERNAME, PASSWORD, PUBLIC_ID)
else:
    print("Could not read credentails.json file")
