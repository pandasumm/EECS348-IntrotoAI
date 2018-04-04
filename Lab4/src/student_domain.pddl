(define (domain nosliw)
  (:requirements :strips :typing)
  (:types 
        role thing -RT 
        hero dragon magic-role agent -role 
        sorceress wizard -magic-role 
        sword pen item diamond -thing 
        town location mountain cave -position)
  (:predicates 	
                (at ?someone -RT ?location -position)
                (different ?s1 ?s2 -thing)
                (possesses ?someone -role ?something -thing)
                (path-from-to ?from ?to -position)
                (asleep ?d -dragon)
                (safe ?t -town)
                (strong ?h -hero)
                (dead ?d -dragon)
  )
         
  
  (:action trade-with-sb
	     :parameters (?h -role ?r -role ?l -position ?t1 ?t2 -thing)
	     :precondition (and 
                (at ?h ?l)
                (at ?r ?l)
                (possesses ?h ?t1)
                (possesses ?r ?t2)
            )
	     :effect (and 
                (possesses ?h ?t2)
                (possesses ?r ?t1)
                (not(possesses ?h ?t1))
                (not(possesses ?r ?t2))
            )
  )

  (:action abtain-from-sp
	     :parameters (?p1  -role ?l -position ?t -thing)
	     :precondition (and 
                (at ?p1 ?l)
                (at ?t ?l)
            )
	     :effect (and 
                (possesses ?p1 ?t)
                (not(at ?t ?l))
            )
  )
  
  (:action go-from-to
	     :parameters (?someone -hero ?from ?to -position)
	     :precondition (and 
                (at ?someone ?from)
                (path-from-to ?from ?to)
            )
	     :effect (and 
                (at ?someone ?to)
                (not(at ?someone ?from))
            )
  )  

  
  (:action trade-for-magic
         :parameters (?h -hero ?p -position ?r -magic-role ?d1 ?d2 ?d3 -diamond)
         :precondition (and
                (possesses ?h ?d1)
                (possesses ?h ?d2)
                (possesses ?h ?d3)
                (different ?d1 ?d2)
                (different ?d1 ?d3)
                (different ?d2 ?d3)
                (at ?h ?p)
                (at ?r ?p)
            )
         :effect( and
                (strong ?h)
                (not(possesses ?h ?d1))
                (not(possesses ?h ?d2))
                (not(possesses ?h ?d3))
                (possesses ?r ?d1)
                (possesses ?r ?d2)
                (possesses ?r ?d3)
         )
  )
  (:action kill-dragon
         :parameters (?h -hero ?d -dragon ?c -cave ?t -town)
         :precondition( and
                (strong ?h)
                (at ?h ?c)
                (at ?d ?c)
                ;(not(asleep ?d))
         )
         :effect( and
                (dead ?d)
                (safe ?t)
                (not(asleep ?d))
         )
  )
  
  (:action sleep-dragon-with-quill
         :parameters (?p -hero ?q -pen ?d -dragon ?t -town)
         :precondition (and
                (possesses ?p ?q)
            )
         :effect( and
                (asleep ?d)
                (safe ?t)
         )
  )
  
)