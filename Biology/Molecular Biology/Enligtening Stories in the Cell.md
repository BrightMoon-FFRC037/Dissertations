# Introduction
As a student major in Integrated Science Program (ISP), I should be living in the **Context of Biology**, especially molecular biology, which is subject to study for us. Meanwhile, I also try to walk through different disciplines including mathematic, physics, chemistry, electrical enginerring and computer science to enrich the my toolkit to solve problems in life science.

In my first year in university, I was amazed by the elegance of physical theory, the rigorous and thorough logical system of mathematics and the widespread applications of electrical engineering and computer science. But what about Biology?

Biology only left me so many things to remember rather than deriving them with logic, which is terrible for me.

What amazing in biology is not the facts, but the reasons behind those facts as well as the principles underlines those meticulous and well disigned mechanisms.

Those enligtening parts of biology can not be discovered or understood without thinking and reflecting. And once I realize them, I find those priciple is universial, not limited to biology itself.

That is the reason why I set up the file to record such thoughts and stories.

# Why DNA Replicates from 5' to 3' ?
## Logic
* Engergy, which is like Olimpic Flame relayed by athletes, is stored at 5' end of each nuleoside. **(Root of the asymmetry)**
* If there is a mistake, self-correction will be carried out by exonulease subunit or protein domain of DNA Polymerase, which leads to the error nuleoside to by cleaved off the strand.
* 
    * 5'$\rightarrow$ 3': the energy is carried by new members (next one). Each for itself, from the aspect of energy.
    * 3'$\rightarrow$ 5': the energy is carried by old members (last one). Each for the next and each relies on the last, from the aspect of energy.
* The necessity of energy (triphosphte in 5' end) entails the old one carring energy cannot be cut off the strand in the case of 3'$\rightarrow$ 5', otherwise the replication will terminate here.
* The 5'$\rightarrow$ 3' mode allows removing any nuleoside added earlier without worrying about energy, since each nuleoside carries energy for itself.
## Inspiration
* Both algorithm work in normal case, but one of them has severe disadvantage considering mistakes and correction.
* The independency allows for more convenient correction, which increases accuracy.
## Connections
* 
    * Correction mechanism implies the direction of replication: 5' to 3'.
    * Reason: The Old Can be Removed.
* 
    * It also implies the RNA primer produced by DNA primase is needed prior to DNA polymerase.
    * Reason: The Subject to be Shecked Exists.

# Why Each Region of the DNA is Replicated Once and Only Once ?
## Logic
* Replication Initiation is **separated into two sequential steps** in eukaryotes.
    * Loading of Helicase. In $G_1$ phase when kinase activity is low.
    * Activating of Helicase. In $S$ phase when kinase activity is high.

* The kinase activity changes from low to high chronologically.

* Each replication origin has at most one chance to form ORC-DNA complex and gets helicase. (Mechanism 1)

* Besides, any ORC-DNA complex passed by a replication fork is inactivated. (Mechanism 2)

## Inspiration

* To prevent the accordingly unactivated to be activated.
    * Just one opportunity to get activated.
    * Mechanism 1: Additional requirements (steps).
* To prevent the already activated to be activated again.
    * Deactivate the already activated one.
    * Mechanism 2
* The **chronologically changing environment makes the process irreversible**, which ensures firing once and only once.


