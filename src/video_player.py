"""A video player class."""

from .video_library import VideoLibrary
import random


class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self.playing = [False, None]
        self.playlist = []
        self.playlist_lower = []
        self.queue = []

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        all_videos = self._video_library.get_all_videos()
        all_videos.sort(key=lambda x: x.title)
        print("Here's a list of all available videos:")
        for video in all_videos:
            tagString = " ".join(video.tags)
            print(f'{video.title} ({video.video_id}) [{tagString}]')
    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """
        video = self._video_library.get_video(video_id)
        if video == None:
            print("Cannot play video: Video does not exist")
            return self.playing

        if self.playing[0] is False:
            print("Playing video: " + video.title)
            self.playing = [True, video.title]
        else:
            print("Stopping video: " + self.playing[1])
            print("Playing video: " + video.title)
            self.playing = [True, video.title]


    def stop_video(self):
        """Stops the current video."""
        currentVideo = self.playing[1]
        if self.playing[1] != None:
            print("Stopping video: " + currentVideo)
            self.playing[1] = None
        else:
            print("Cannot stop video: No video is currently playing")



    def play_random_video(self):
        """Plays a random video from the video library."""
        video = random.choice(self._video_library.get_all_videos())
        if self.playing[0] is True:
            print("Stopping video: " + self.playing[1])
            self.playing[1] = video.title
            print("Playing video: " + self.playing[1])
        else:
            self.playing[1] = video.title
            print("Playing video: " + self.playing[1])



    def pause_video(self):
        """Pauses the current video."""

        if self.playing[1] == None:
            print("Cannot pause video: No video is currently playing")
            return self.playing
        else:
            print("Pausing video: " + self.playing[1])

    def continue_video(self):
        """Resumes playing the current video."""

        if self.playing[1] == None:
            print("Cannot continue video: No video is currently playing")
            return self.playing
        else:
            print("Continuing video: " + self.playing[1])


    def show_playing(self):
        """Displays video currently playing."""
        if self.playing[1] == None:
            print("No video is currently playing")
        else:
            print("Currently playing: " + self.playing[1])


    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        if playlist_name.lower() in self.playlist_lower:
            print("Cannot create playlist: A playlist with the same name already "
            "exists")
        else:
            print("Successfully created new playlist: " + playlist_name)
            self.playlist.append(playlist_name)
            self.playlist_lower.append(playlist_name.lower())





    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        video = self._video_library.get_video(video_id)
        self.playlist.append(playlist_name)
        
        if video_id in self.queue:
            print(f"Cannot add video to {playlist_name}: Video already added")
        elif video == None:
            print(f"Cannot add video to {playlist_name}: Video does not exist")
        else:
            print(f'Added video to {playlist_name}: {video.title}')
            self.queue.append(video_id)


    def show_all_playlists(self):
        """Display all playlists."""

        print("Showing all playlists:")
        for playlist in self.playlist:
            print(playlist)


    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print(f'Showing playlist: {playlist_name}')
        if self.queue == None:
            print("No videos here yet")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        vidlist = self._video_library.get_all_videos()
        print(f"Here are the results for {search_term}:")
        for video in vidlist:
            if str(search_term) in video.tags:
                print(video)

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print(f"Here are the results for {video_tag}:")


    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")

