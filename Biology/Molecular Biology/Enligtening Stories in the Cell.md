# Introduction
As a student major in Integrated Science Program (ISP), I should be living in the **Context of Biology**, especially molecular biology, which is subject to study for us. Meanwhile, I also try to walk through different disciplines including mathematic, physics, chemistry, electrical enginerring and computer science to enrich the my toolkit to solve problems in life science.

In my first year in university, I was amazed by the elegance of physical theory, the rigorous and thorough logical system of mathematics and the widespread applications of electrical engineering and computer science. But what about Biology?

Biology only left me so many things to remember rather than deriving them with logic, which is terrible for me.

What amazing in biology is not the facts, but the reasons behind those facts as well as the principles underlines those meticulous and well disigned mechanisms.

Those enlightening parts of biology can not be discovered or understood without thinking and reflecting. And once I realize them, I find those priciple is universial, not limited to biology itself.

That is the reason why I set up the file to record such thoughts and stories.

# Why DNA Replicates from 5' to 3' ?
## Logic
* Energy, which is like Olimpic Flame relayed by athletes, is stored at 5' end of each nuleoside. **(Root of the asymmetry)**
* If there is a mistake, self-correction will be carried out by exonulease subunit or protein domain of DNA Polymerase, which leads to the error nuleoside to by cleaved off the strand.
* 
    * 5' $\rightarrow$ 3': the energy is carried by new members (next one). Each for itself, from the aspect of energy.
    * 3' $\rightarrow$ 5': the energy is carried by old members (last one). Each for the next and each relies on the last, from the aspect of energy.
* The necessity of energy (triphosphate in 5' end) entails the old one carring energy cannot be cut off the strand in the case of 3'$\rightarrow$ 5', otherwise the replication will terminate here.
* The 5' $\rightarrow$ 3' mode allows removing any nucleoside added earlier without worrying about energy, since each nuleoside carries energy for itself.
## Inspiration
* Both algorithm work in normal case, but one of them has severe disadvantage considering mistakes and correction.
* The independency allows for more convenient correction, which increases accuracy.
## Connections
* 
    * Correction mechanism implies the direction of replication: 5' to 3'.
    * Reason: The Old Can be Removed.
* 
    * It also implies the RNA primer produced by DNA primase is needed prior to DNA polymerase.
    * Reason: The Subject to be Checked Exists.

# Why Each Region of the DNA is Replicated Once and Only Once ?
## Logic
* Replication Initiation is **separated into two sequential steps** in eukaryotes.
    * Loading of Helicase. In $G_1$ phase when kinase activity is low.
    * Activating of Helicase. In $S$ phase when kinase activity is high.

* The kinase activity changes from low to high chronologically.

* Each replication origin has at most one chance to form ORC-DNA complex and gets helicase. (Mechanism 1)

* Besides, any ORC-DNA complex passed by a replication fork is inactivated. (Mechanism 2)

## Inspiration

* To prevent the accordingly inactivated to be activated.
    * Just one opportunity to get activated.
    * Mechanism 1: Additional requirements (steps).
* To prevent the already activated to be activated again.
    * Deactivate the already activated one.
    * Mechanism 2
* The **chronologically changing environment makes the process irreversible**, which ensures firing once and only once.

# The Supercoils Caused by RNA Polymerase is Useful !

## Logic
* The elongation of RNA Polymerase builds up tension in DNA causing supercoil of it.
* The supercoil can facilitate the partial unwrapping of the DNA in nuleosomes.

## Inspiration
* **Productive use of cast-off things** is an eternal theme in the natrual world and there are several common forms of this kind of utilization:
  * Reuse the **energy (E)** especially heat.
  * Reuse the **materials (m)** especially in chemical industry.
  * Reuse the **force (F)** or **moment (M)** which occurs to me firstly in this case. 

# Transporting Cargo through Barrier need Intermediary and Recycle
## Examples
* **cholesterol** *through* cell membrane
  * cell membrane
    * LDL receptor
  * intermediary
    * LDL low density lipoprotein
      * bind to cholesterol in blood
      * release cholesterol in endosome
      * LDL itself is degraded in endosome
  * cholesterol
* **Iron** *through* cell membrane
  * cell membrane
    * transferrin receptor
  * intermediary
    * transferrin
      * bind to iron at neutral pH in blood
      * release iron at acidic pH in endosome
      * recycle of transferrin by pH *difference*
  * iron
* **nuclear proteins** *through* nuclear pores
  * nuclear pores
    * NPC nuclear pore complex meshwork
    * nuclear basket
  * intermediary
    * nuclear import receptor (bind to cargo)
    * recycle of import receptor by Ran-GTP and Ran-GDP
    * Ran-GTP (release cargo)
    * recycle of Ran-GTP by 
      * Ran-GAP (GTPase-activating protein)
      * Ran-GEF (GTP exchange factor)
  * nuclear proteins 
    * nuclear localization signal
  
## Logic
> When the cell wants to transport C(cargo) through B(barrier) there must be a pair of opposite processes,
> one of them load the cargo while the other one release the cargo.
> That reflects a reversible binding process, which must be carried out at different conditions.
> For example the pH differences and the existence of Ran-GAP and Ran-GTP.
> Meanwhile, how to maintain that difference is another problem including the proton pump and recycle of Ran-GTP...

