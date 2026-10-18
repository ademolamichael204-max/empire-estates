rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {

    function signedIn() { return request.auth != null; }

    
    function isAdmin() {
      return signedIn() && exists(/databases/$(database)/documents/admins/$(request.auth.uid));
    }

  
    match /admins/{uid} {
      allow get: if signedIn() && request.auth.uid == uid;
      allow write: if false;
    }

    match /listings/{id} {
      allow read: if true;
      allow write: if isAdmin();
      match /media/{mid} {
        allow read: if true;
        allow write: if isAdmin();
      }
    }
    match /announcements/{id} {
      allow read: if true;
      allow write: if isAdmin();
    }
    match /settings/{id} {
      allow read: if true;
      allow write: if isAdmin();
    }

   
    match /users/{uid} {
      allow read: if signedIn() && (request.auth.uid == uid || isAdmin());
      allow create: if signedIn() && request.auth.uid == uid;
      allow update: if signedIn() && request.auth.uid == uid;
      allow delete: if isAdmin();
    }

    match /requests/{id} {
      allow create: if signedIn()
                    && request.resource.data.uid == request.auth.uid
                    && request.resource.data.status == 'pending'
                    && request.resource.data.verified == false;
      allow read: if signedIn() && (resource.data.uid == request.auth.uid || isAdmin());
      allow update, delete: if isAdmin();
    }

    
    match /threads/{uid} {
      allow read, write: if signedIn() && (request.auth.uid == uid || isAdmin());
      match /messages/{mid} {
        allow read: if signedIn() && (request.auth.uid == uid || isAdmin());
        allow create: if signedIn() && (request.auth.uid == uid || isAdmin())
                      && request.resource.data.from == request.auth.uid;
        allow delete: if isAdmin();
      }
    }
  }
}