import tweepy
from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel

class OAuth1AuthConfig(BaseModel):
    consumer_key: str
    consumer_secret: str
    access_token: str
    access_token_secret: str

class Executor:
    @staticmethod
    def create_client(
        auth: OAuth1AuthConfig,
        return_type: Union[type, Dict] = dict,
        **kwargs
    ) -> tweepy.Client:
        """
        Creates and returns a Tweepy Client instance using the provided authentication credentials.
        The `return_type` parameter determines the format of the responses.
        
        Parameters:
            auth (OAuth1AuthConfig): Twitter API OAuth 1.0a Authentication Configuration.
            return_type (type or dict, optional): Determines the response format. Defaults to dict.
            **kwargs (dict): Additional keyword arguments for Tweepy Client initialization.

        Returns:
            tweepy.Client: Configured Tweepy Client.
        """
        client = tweepy.Client(
            consumer_key=auth.consumer_key,
            consumer_secret=auth.consumer_secret,
            access_token=auth.access_token,
            access_token_secret=auth.access_token_secret,
            return_type=return_type,
            **kwargs
        )
        return client

    # Tweet Methods
    @staticmethod
    def twitter_tweets_get(
        auth: OAuth1AuthConfig,
        ids: Union[str, List[str]],
        **kwargs
    ) -> Dict[str, Any]:
        client = Executor.create_client(auth, **kwargs)
        return client.get_tweets(ids=ids, **kwargs)

    @staticmethod
    def twitter_tweets_post(
        auth: OAuth1AuthConfig,
        text: str,
        **kwargs
    ) -> Dict[str, Any]:
        client = Executor.create_client(auth, **kwargs)
        return client.create_tweet(text=text, **kwargs)

    @staticmethod
    def twitter_tweets_counts_all_get(
        auth: OAuth1AuthConfig,
        query: str,
        **kwargs
    ) -> Dict[str, Any]:
        client = Executor.create_client(auth, **kwargs)
        return client.get_all_tweets_count(query=query, **kwargs)

    @staticmethod
    def twitter_tweets_counts_recent_get(
        auth: OAuth1AuthConfig,
        query: str,
        **kwargs
    ) -> Dict[str, Any]:
        client = Executor.create_client(auth, **kwargs)
        return client.get_recent_tweets_count(query=query, **kwargs)

    # @staticmethod
    # def twitter_tweets_search_stream_get(
    #     bearer_token: str,
    #     **kwargs
    # ) -> Dict[str, Any]:
    #     client = Executor.create_client(bearer_token, **kwargs)
    #     return client.get_filtered_stream(**kwargs)

    # @staticmethod
    # def twitter_tweets_search_stream_rules_post(
    #     bearer_token: str,
    #     add: List[Dict[str, str]],
    #     **kwargs
    # ) -> Dict[str, Any]:
    #     client = Executor.create_client(bearer_token, **kwargs)
    #     return client.add_rules(add=add, **kwargs)

    # @staticmethod
    # def twitter_tweets_search_stream_rules_get(
    #     bearer_token: str,
    #     **kwargs
    # ) -> Dict[str, Any]:
    #     client = Executor.create_client(bearer_token, **kwargs)
    #     return client.get_rules(**kwargs)

    @staticmethod
    def twitter_tweets_id_delete(
        auth: OAuth1AuthConfig,
        id: str,
        **kwargs
    ) -> Dict[str, Any]:
        client = Executor.create_client(auth, **kwargs)
        return client.delete_tweet(id=id, **kwargs)

    @staticmethod
    def twitter_tweets_id_get(
        auth: OAuth1AuthConfig,
        id: str,
        **kwargs
    ) -> Dict[str, Any]:
        client = Executor.create_client(auth, **kwargs)
        return client.get_tweet(id=id, **kwargs)

    @staticmethod
    def twitter_tweets_id_liking_users_get(
        auth: OAuth1AuthConfig,
        id: str,
        **kwargs
    ) -> Dict[str, Any]:
        client = Executor.create_client(auth, **kwargs)
        return client.get_liking_users(id=id, **kwargs)

    @staticmethod
    def twitter_tweets_id_quote_tweets_get(
        auth: OAuth1AuthConfig,
        id: str,
        **kwargs
    ) -> Dict[str, Any]:
        client = Executor.create_client(auth, **kwargs)
        return client.get_quote_tweets(id=id, **kwargs)

    @staticmethod
    def twitter_tweets_id_retweeted_by_get(
        auth: OAuth1AuthConfig,
        id: str,
        **kwargs
    ) -> Dict[str, Any]:
        client = Executor.create_client(auth, **kwargs)
        return client.get_retweeters(id=id, **kwargs)

    # @staticmethod
    # def twitter_tweets_sample_stream_get(
    #     bearer_token: str,
    #     **kwargs
    # ) -> Dict[str, Any]:
    #     client = Executor.create_client(bearer_token, **kwargs)
    #     return client.sample_stream(**kwargs)

    @staticmethod
    def twitter_tweets_search_all_get(
        auth: OAuth1AuthConfig,
        query: str,
        **kwargs
    ) -> Dict[str, Any]:
        client = Executor.create_client(auth, **kwargs)
        return client.search_all_tweets(query=query, **kwargs)

    @staticmethod
    def twitter_tweets_search_recent_get(
        auth: OAuth1AuthConfig,
        query: str,
        **kwargs
    ) -> Dict[str, Any]:
        client = Executor.create_client(auth, **kwargs)
        return client.search_recent_tweets(query=query, **kwargs)

    # User Methods
    @staticmethod
    def twitter_users_get(
        auth: OAuth1AuthConfig,
        ids: Union[str, List[str]],
        **kwargs
    ) -> Dict[str, Any]:
        client = Executor.create_client(auth, **kwargs)
        return client.get_users(ids=ids, **kwargs)

    @staticmethod
    def twitter_users_by_get(
        auth: OAuth1AuthConfig,
        **kwargs
    ) -> Dict[str, Any]:
        # Assuming this is similar to getting users by various parameters
        client = Executor.create_client(auth, **kwargs)
        return client.get_users(**kwargs)

    @staticmethod
    def twitter_users_by_username_username_get(
        auth: OAuth1AuthConfig,
        username: str,
        **kwargs
    ) -> Dict[str, Any]:
        client = Executor.create_client(auth, **kwargs)
        return client.get_user(username=username, **kwargs)

    @staticmethod
    def twitter_users_id_get(
        auth: OAuth1AuthConfig,
        id: str,
        **kwargs
    ) -> Dict[str, Any]:
        client = Executor.create_client(auth, **kwargs)
        return client.get_user(id=id, **kwargs)

    @staticmethod
    def twitter_users_id_blocking_get(
        auth: OAuth1AuthConfig,
        id: str,
        **kwargs
    ) -> Dict[str, Any]:
        client = Executor.create_client(auth, **kwargs)
        return client.get_blocked(id=id, **kwargs)

    @staticmethod
    def twitter_users_id_blocking_post(
        auth: OAuth1AuthConfig,
        id: str,
        **kwargs
    ) -> Dict[str, Any]:
        client = Executor.create_client(auth, **kwargs)

        response = client.request(
            method="POST",
            url=f"https://api.twitter.com/2/users/{id}/blocking",
            json=kwargs
        )
        return response
    
    @staticmethod
    def twitter_users_source_user_id_blocking_target_user_id_delete(
        auth: OAuth1AuthConfig,
        source_user_id: str,
        target_user_id: str,
        **kwargs
    ) -> Dict[str, Any]:
        client = Executor.create_client(auth, **kwargs)
        url = f"https://api.twitter.com/2/users/{source_user_id}/blocking/{target_user_id}"
        return client.request(
            method="DELETE",
            url=url,
        )
    
    @staticmethod
    def twitter_users_id_bookmarks_get(
        auth: OAuth1AuthConfig,
        **kwargs
    ) -> Dict[str, Any]:
        client = Executor.create_client(auth, **kwargs)
        return client.get_bookmarks(**kwargs)

    @staticmethod
    def twitter_users_id_bookmarks_post(
        auth: OAuth1AuthConfig,
        tweet_id: str,
        **kwargs
    ) -> Dict[str, Any]:
        client = Executor.create_client(auth, **kwargs)
        return client.bookmark(tweet_id=tweet_id, **kwargs)

    @staticmethod
    def twitter_users_id_bookmarks_tweet_id_delete(
        auth: OAuth1AuthConfig,
        id: str,
        tweet_id: str,
        **kwargs
    ) -> Dict[str, Any]:
        client = Executor.create_client(auth, **kwargs)
        response = client.request(
            method="DELETE",
            url=f"https://api.twitter.com/2/users/{id}/bookmarks/{tweet_id}",
        )
        return response

    @staticmethod
    def twitter_users_id_followed_lists_get(
        auth: OAuth1AuthConfig,
        id: str,
        **kwargs
    ) -> Dict[str, Any]:
        client = Executor.create_client(auth, **kwargs)
        return client.get_followed_lists(id=id, **kwargs)

    @staticmethod
    def twitter_users_id_followed_lists_post(
        auth: OAuth1AuthConfig,
        id: str,
        list_id: str,
        **kwargs
    ) -> Dict[str, Any]:
        client = Executor.create_client(auth, **kwargs)
        return client.follow_list(id=id, list_id=list_id, **kwargs)

    @staticmethod
    def twitter_users_id_followed_lists_list_id_delete(
        auth: OAuth1AuthConfig,
        id: str,
        list_id: str,
        **kwargs
    ) -> Dict[str, Any]:
        client = Executor.create_client(auth, **kwargs)
        response = client.request(
            method="DELETE",
            url=f"https://api.twitter.com/2/users/{id}/followed_lists/{list_id}",
        )
        return response

    @staticmethod
    def twitter_users_id_followers_get(
        auth: OAuth1AuthConfig,
        id: str,
        **kwargs
    ) -> Dict[str, Any]:
        client = Executor.create_client(auth, **kwargs)
        return client.get_users_followers(id=id, **kwargs)

    @staticmethod
    def twitter_users_id_following_get(
        auth: OAuth1AuthConfig,
        id: str,
        **kwargs
    ) -> Dict[str, Any]:
        client = Executor.create_client(auth, **kwargs)
        return client.get_users_following(id=id, **kwargs)

    @staticmethod
    def twitter_users_id_following_post(
        auth: OAuth1AuthConfig,
        id: str,
        **kwargs
    ) -> Dict[str, Any]:
        client = Executor.create_client(auth, **kwargs)
        response = client.request(
            method="POST",
            url=f"https://api.twitter.com/2/users/{id}/following",
            json=kwargs,
        )
        return response

    @staticmethod
    def twitter_users_source_user_id_following_target_user_id_delete(
        auth: OAuth1AuthConfig,
        source_user_id: str,
        **kwargs
    ) -> Dict[str, Any]:
        client = Executor.create_client(auth, **kwargs)
        response = client.request(
            method="POST",
            url=f"https://api.twitter.com/2/users/{source_user_id}/following",
            json=kwargs,
        )
        return response

    @staticmethod
    def twitter_users_id_liked_tweets_get(
        auth: OAuth1AuthConfig,
        id: str,
        **kwargs
    ) -> Dict[str, Any]:
        client = Executor.create_client(auth, **kwargs)
        return client.get_liked_tweets(id=id, **kwargs)

    @staticmethod
    def twitter_users_id_likes_post(
        auth: OAuth1AuthConfig,
        tweet_id: str,
        **kwargs
    ) -> Dict[str, Any]:
        client = Executor.create_client(auth, **kwargs)
        return client.like(tweet_id=tweet_id, **kwargs)

    @staticmethod
    def twitter_users_id_likes_tweet_id_delete(
        auth: OAuth1AuthConfig,
        tweet_id: str,
        **kwargs
    ) -> Dict[str, Any]:
        client = Executor.create_client(auth, **kwargs)
        return client.unlike(tweet_id=tweet_id)

    @staticmethod
    def twitter_users_id_list_memberships_get(
        auth: OAuth1AuthConfig,
        id: str,
        **kwargs
    ) -> Dict[str, Any]:
        client = Executor.create_client(auth, **kwargs)
        return client.get_list_memberships(id=id, **kwargs)

    @staticmethod
    def twitter_users_id_mentions_get(
        auth: OAuth1AuthConfig,
        id: str,
        **kwargs
    ) -> Dict[str, Any]:
        client = Executor.create_client(auth, **kwargs)
        return client.get_users_mentions(id=id, **kwargs)

    @staticmethod
    def twitter_users_id_muting_get(
        auth: OAuth1AuthConfig,
        id: str,
        **kwargs
    ) -> Dict[str, Any]:
        client = Executor.create_client(auth, **kwargs)
        return client.get_muted(id=id, **kwargs)

    @staticmethod
    def twitter_users_id_muting_post(
        auth: OAuth1AuthConfig,
        target_user_id: str,
        **kwargs
    ) -> Dict[str, Any]:
        client = Executor.create_client(auth, **kwargs)
        return client.mute(target_user_id=target_user_id, **kwargs)

    @staticmethod
    def twitter_users_source_user_id_muting_target_user_id_delete(
        auth: OAuth1AuthConfig,
        target_user_id: str,
        **kwargs
    ) -> Dict[str, Any]:
        client = Executor.create_client(auth, **kwargs)
        return client.unmute(target_user_id=target_user_id, **kwargs)

    @staticmethod
    def twitter_users_id_owned_lists_get(
        auth: OAuth1AuthConfig,
        id: str,
        **kwargs
    ) -> Dict[str, Any]:
        client = Executor.create_client(auth, **kwargs)
        return client.get_owned_lists(id=id, **kwargs)

    @staticmethod
    def twitter_users_id_pinned_lists_get(
        auth: OAuth1AuthConfig,
        id: str,
        **kwargs
    ) -> Dict[str, Any]:
        client = Executor.create_client(auth, **kwargs)
        return client.get_pinned_lists(**kwargs)

    @staticmethod
    def twitter_users_id_pinned_lists_post(
        auth: OAuth1AuthConfig,
        id: str,
        list_id: str,
        **kwargs
    ) -> Dict[str, Any]:
        client = Executor.create_client(auth, **kwargs)
        return client.pin_list(list_id=list_id, **kwargs)


    @staticmethod
    def twitter_users_id_retweets_post(
        auth: OAuth1AuthConfig,
        tweet_id: str,
        **kwargs
    ) -> Dict[str, Any]:
        client = Executor.create_client(auth, **kwargs)
        return client.retweet(tweet_id=tweet_id, **kwargs)

    @staticmethod
    def twitter_users_id_retweets_source_tweet_id_delete(
        auth: OAuth1AuthConfig,
        source_tweet_id: str,
        **kwargs
    ) -> Dict[str, Any]:
        client = Executor.create_client(auth, **kwargs)
        return client.unretweet(source_tweet_id=source_tweet_id, **kwargs)

    @staticmethod
    def twitter_users_id_timelines_reverse_chronological_get(
        auth: OAuth1AuthConfig,
        id: str,
        **kwargs
    ) -> Dict[str, Any]:
        client = Executor.create_client(auth, **kwargs)
        return client.get_home_timeline(user_id=id, **kwargs)

    @staticmethod
    def twitter_users_id_tweets_get(
        auth: OAuth1AuthConfig,
        id: str,
        **kwargs
    ) -> Dict[str, Any]:
        client = Executor.create_client(auth, **kwargs)
        return client.get_users_tweets(id=id, **kwargs)

    # List Methods
    @staticmethod
    def twitter_lists_post(
        auth: OAuth1AuthConfig,
        name: str,
        **kwargs
    ) -> Dict[str, Any]:
        client = Executor.create_client(auth, **kwargs)
        return client.create_list(name=name, **kwargs)

    @staticmethod
    def twitter_lists_id_get(
        auth: OAuth1AuthConfig,
        id: str,
        **kwargs
    ) -> Dict[str, Any]:
        client = Executor.create_client(auth, **kwargs)
        return client.get_list(id=id, **kwargs)

    @staticmethod
    def twitter_lists_id_delete(
        auth: OAuth1AuthConfig,
        id: str,
        **kwargs
    ) -> Dict[str, Any]:
        client = Executor.create_client(auth, **kwargs)
        return client.delete_list(id=id, **kwargs)

    @staticmethod
    def twitter_lists_id_put(
        auth: OAuth1AuthConfig,
        id: str,
        **kwargs
    ) -> Dict[str, Any]:
        client = Executor.create_client(auth, **kwargs)
        return client.update_list(id=id, **kwargs)

    @staticmethod
    def twitter_lists_id_followers_get(
        auth: OAuth1AuthConfig,
        id: str,
        **kwargs
    ) -> Dict[str, Any]:
        client = Executor.create_client(auth, **kwargs)
        return client.get_list_followers(id=id, **kwargs)

    @staticmethod
    def twitter_lists_id_members_get(
        auth: OAuth1AuthConfig,
        id: str,
        **kwargs
    ) -> Dict[str, Any]:
        client = Executor.create_client(auth, **kwargs)
        return client.get_list_members(id=id, **kwargs)

    @staticmethod
    def twitter_lists_id_members_post(
        auth: OAuth1AuthConfig,
        id: str,
        user_id: str,
        **kwargs
    ) -> Dict[str, Any]:
        client = Executor.create_client(auth, **kwargs)
        return client.add_list_member(id=id, user_id=user_id, **kwargs)

    @staticmethod
    def twitter_lists_id_members_user_id_delete(
        auth: OAuth1AuthConfig,
        id: str,
        user_id: str,
        **kwargs
    ) -> Dict[str, Any]:
        client = Executor.create_client(auth, **kwargs)
        return client.remove_list_member(id=id, user_id=user_id, **kwargs)

    @staticmethod
    def twitter_lists_id_tweets_get(
        auth: OAuth1AuthConfig,
        id: str,
        **kwargs
    ) -> Dict[str, Any]:
        client = Executor.create_client(auth, **kwargs)
        return client.get_list_tweets(id=id, **kwargs)

    # Compliance Methods
    @staticmethod
    def twitter_compliance_jobs_post(
        auth: OAuth1AuthConfig,
        type: str,
        **kwargs
    ) -> Dict[str, Any]:
        client = Executor.create_client(auth, **kwargs)
        return client.create_compliance_job(type=type, **kwargs)

    @staticmethod
    def twitter_compliance_jobs_get(
        auth: OAuth1AuthConfig,
        **kwargs
    ) -> Dict[str, Any]:
        client = Executor.create_client(auth, **kwargs)
        return client.get_compliance_jobs(**kwargs)

    @staticmethod
    def twitter_compliance_jobs_id_get(
        auth: OAuth1AuthConfig,
        id: str,
        **kwargs
    ) -> Dict[str, Any]:
        client = Executor.create_client(auth, **kwargs)
        return client.get_compliance_job(id=id, **kwargs)
    
    # Space Methods
    @staticmethod
    def twitter_spaces_get(
        auth: OAuth1AuthConfig,
        ids: Union[str, List[str]],
        **kwargs
    ) -> Dict[str, Any]:
        client = Executor.create_client(auth, **kwargs)
        return client.get_spaces(ids=ids, **kwargs)

    @staticmethod
    def twitter_spaces_search_get(
        auth: OAuth1AuthConfig,
        query: str,
        **kwargs
    ) -> Dict[str, Any]:
        client = Executor.create_client(auth, **kwargs)
        return client.search_spaces(query=query, **kwargs)

    @staticmethod
    def twitter_spaces_id_get(
        auth: OAuth1AuthConfig,
        id: str,
        **kwargs
    ) -> Dict[str, Any]:
        client = Executor.create_client(auth, **kwargs)
        return client.get_space(id=id, **kwargs)

    @staticmethod
    def twitter_spaces_id_buyers_get(
        auth: OAuth1AuthConfig,
        id: str,
        **kwargs
    ) -> Dict[str, Any]:
        client = Executor.create_client(auth, **kwargs)
        return client.get_space_buyers(id=id, **kwargs)

    # DM (Direct Message) Methods
    @staticmethod
    def twitter_dm_conversation_id_create(
        auth: OAuth1AuthConfig,
        **kwargs
    ) -> Dict[str, Any]:
        # TODO: Add support for multiple attachments
        client = Executor.create_client(auth, **kwargs)
        args = {
            "participant_ids": kwargs["participant_ids"]
        }
        
        if kwargs.get("attachments"):
            if isinstance(kwargs.get("attachments"), list):
                if len(kwargs.get("attachments")) > 1:
                    raise ValueError("Only one attachment is supported for DM conversations")
                args["media_id"] = kwargs.get("attachments")[0]["media_id"]
        if kwargs.get("text"):
            args["text"] = kwargs["text"]
        return client.create_direct_message_conversation(**args)

    @staticmethod
    def twitter_dm_events_get(
        auth: OAuth1AuthConfig,
        **kwargs
    ) -> Dict[str, Any]:
        client = Executor.create_client(auth, **kwargs)
        return client.get_direct_message_events(**kwargs)
    
    @staticmethod
    def twitter_dm_conversations_with_participant_id_dm_events_get(
        auth: OAuth1AuthConfig,
        participant_id: str,
        **kwargs
    ) -> Dict[str, Any]:
        client = Executor.create_client(auth, **kwargs)
        return client.get_direct_message_events(participant_id=participant_id, **kwargs)

    @staticmethod
    def twitter_find_my_user(
        auth: OAuth1AuthConfig,
        **kwargs
    ) -> Dict[str, Any]:
        client = Executor.create_client(auth, **kwargs)
        return client.get_me(**kwargs)

    @staticmethod
    def twitter_list_user_unpin(
        auth: OAuth1AuthConfig,
        list_id: str,
        **kwargs
    ) -> Dict[str, Any]:
        client = Executor.create_client(auth, **kwargs)
        return client.unpin_list(list_id=list_id, **kwargs)

    @staticmethod
    def twitter_hide_reply_by_id(
        auth: OAuth1AuthConfig,
        tweet_id: str,
        **kwargs
    ) -> Dict[str, Any]:
        client = Executor.create_client(auth, **kwargs)
        return client.hide_reply(tweet_id=tweet_id, **kwargs)

    @staticmethod
    def twitter_find_spaces_by_creator_ids(
        auth: OAuth1AuthConfig,
        user_ids: List[str],
        **kwargs
    ) -> Dict[str, Any]:
        client = Executor.create_client(auth, **kwargs)
        return client.get_spaces(user_ids=user_ids, **kwargs)

    @staticmethod
    def twitter_get_dm_conversations_id_dm_events(
        auth: OAuth1AuthConfig,
        **kwargs
    ) -> Dict[str, Any]:
        client = Executor.create_client(auth, **kwargs)
        return client.get_direct_message_events(dm_conversation_id=kwargs["id"], **kwargs)

    @staticmethod
    def twitter_dm_conversations_with_participant_id_messages_post(
        auth: OAuth1AuthConfig,
        participant_id: str,
        text: str,
        **kwargs
    ) -> Dict[str, Any]:
        client = Executor.create_client(auth, **kwargs)
        return client.create_direct_message(participant_id=participant_id, text=text, **kwargs)

    @staticmethod
    def twitter_dm_conversations_dm_conversation_id_messages_post(
        auth: OAuth1AuthConfig,
        dm_conversation_id: str,
        **kwargs
    ) -> Dict[str, Any]:
        client = Executor.create_client(auth, **kwargs)
        args = {
            "dm_conversation_id": dm_conversation_id
        }
        
        if kwargs.get("attachments"):
            if isinstance(kwargs.get("attachments"), list):
                if len(kwargs.get("attachments")) > 1:
                    raise ValueError("Only one attachment is supported for DM conversations")
                args["media_id"] = kwargs.get("attachments")[0]["media_id"]
        if kwargs.get("text"):
            args["text"] = kwargs["text"]
        return client.create_direct_message(**args)
